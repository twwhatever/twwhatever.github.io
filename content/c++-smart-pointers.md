Overview of C++ smart pointers.

REDO THIS: "FACTORY" style object for unique pointer, smart pointer and weak pointer.  also provide a single example for each

The problem:

````c++
class C {...};

C* get_c() {
    C* ptr = new C();

    return ptr;
};
````

The issue is that to ensure there are no memory (and potentially other resource) leaks, the caller must be sure to call ```` delete ```` on the returned pointer.  In general, designers of C++ libraries try to ensure that all allocated objects are manageable by the caller either by requiring that calling code itself call ```` new ```` or by attaching objects to existing interface objects so that they are transitively managed by proper management of those objects.

The word often used to describe this relationship is *ownership*.  In the case below, object 0 owns the vector.

````c++
class O {

public:
    O() : v_(new std::vector<int>()) {}
    ~O() { delete v_; }

    std::vector<int>* v() { return v_; }
private:
    std::vector<int>* v_;
};
````

A key constraint introduced by this relationship is that any caller of ````O::v```` must not use the pointer after the associated ````O```` object has been destroyed.  In many cases this constraint does not impose a significant burden, but in some cases it is problematic.  For example, if several clients should share one ````O```` object, the developer needs to design a system to ensure that the lifetime of the ````O```` object exceeds the lifetime of the clients.

*Shared pointers*, such as ````std::shared_ptr````, remove this constraint by allowing multiple objects to share ownership.

````c++
class S {

public:
    S(): v_(std::make_shared(new std::vector<int>())) {}
    // Note: default destructor is sufficient for this object

    std::shared_ptr<std::vector<int>> v() { return v_; }

private:
    std::shared_ptr<std::vector<int>> v_;
};
````

Objects pointed to by shared pointers are deleted only when all of the shared pointers that reference the same object are destroyed[^1].

Shared pointers are useful for objects that need to be referenced by consumers whose lifetimes you do not wish to relate.  Another common case is that you want to ensure that a single owner is responsible for an object, but you wish to allow that ownership to be transferred.

````c++
class U {

public:
    U() {}

    std::unique_ptr<std::vector<int>> v() { return make_unique(new std::vector<int>()); }

    // Note: there's no point in keeping the vector as a private variable here for this example, since it would just be transferred when v() is called
};
````

Weak pointers are used when you wish to provide a pointer to something held by a shared pointer withot taking ownership of it.  A weak pointer may bepreferable to a raw pointer for this purpose because it ensures the shared pointer is live prior to accessing the object.

[//]: # Footnotes

[^1]: There is an important technical caveat to this statement, however.  The smart pointers themselves must be copied, not the contents of the smart     pointer.
    For example, this works
    ````c++
    std::shared_ptr<int> copy;
    {
        std::shared_ptr<int> orig = std::make_shared(new int(42));

        // Assignment operator increments the reference count
        copy = orig;

        // When orig goes out of scope, the reference count is still > 0 so the memory is not freed
    }
    std::cout << *copy << endl;
    ````
    But this doesn't
    ````c++
    std::shared_ptr<int> copy;
    {
        std::shared_ptr<int> orig = std::make_shared(new int(42));

        // The reference count never gets updated
        copy.set(orig.get());

        // When orig goes out of scope, the memory is freed
    }

    // Now copy points to freed memory
    std::cout << *copy << endl;
    ````
    
    
