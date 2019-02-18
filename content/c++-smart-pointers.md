Overview of C++ smart pointers.

REDO THIS: "FACTORY" style object for unique pointer, smart pointer and weak pointer.  also provide a single example for each

The problem[^2]:

````c++

std::vector<int>* get_v() {
    return new std::vector<int>(1, 42);
};
````

The issue is that to ensure there are no memory (and potentially other resource) leaks, the caller must be sure to call ```` delete ```` on the returned pointer.  I'll use a block scope to be precise about the problem, but in general this issue comes in to play when different objects need access to the same data.

````c++
std::vector<int>* copy;

{
    std::vector<int>* orig = get_v();
    copy = orig;

    // Can't call delete here (unless you copy v)
}

std::cout << *copy[0] << std::endl;

// Have to remember to call delete 
delete copy;
````

A much more standard approach to the problem is to have an object manage the lifetime of the vector.

````c++
class VOwner {
    std::vector<int> v_;
public:
    VOwner() : v_(1, 42) {}

    // Returning a pointer for consistency, but a reference might be a better idea in practice
    std::vector<int>* get_v() { return v_; }
};
````

In this case, we say that the ````VOwner```` object *owns* the vector.  While that removes the need to delete the vector, the user must now ensure that the VOwner object has a longer lifetime than any caller of ````VOwner::get_v````.

````c++
std::vector<int>* copy;

{
    VOwner orig;
    copy = orig.get_v();
    // Oops, vector gets cleared when orig goes out of scope
}

// Kaboom
std::cout << *copy[0] << std::endl;
````

In many cases it isn't hard to structure the program so that the owner object can outlast all of its users.  However, this structure can be burdensome in cases where lifetime dependencies are hard to unravel, or worse, fundamentally entangled.

Smart pointers implement ownership in a way that allows it to be decoupled with object lifetimes.

# Unique pointers

Unique pointers (````std::unique_ptr<T>````) ensure that an object has exactly one owner.  It is possible to change the owner by copying, assigning or moving the unique pointer.  That allows us to safely implement the original example[^1].

````c++
std::unqiue_ptr<vector<int>> get_unique_v() {
    return std::make_unique(vector<int>(1, 42));
}

std::unique_ptr<vector<int>> copy;

{
    std::unique_ptr<vector<int>> orig = get_unique_v();
    // Ownership is now associated with copy instead of orig.  Note that after this statement
    // orig can no longer be used to access the vector
    copy = orig;
}

std::cout << *copy[0] std::endl;

// The vector will be freed when copy goes out of scope, no need to manually call delete
````

# Shared pointers

Unique pointers are appropriate when you wish to describe transfer of ownership, but another common case is that a single object instance needs to be shared by multiple clients.  This capability is useful when the instance in question is expensive to construct, for example.  Shared pointers (````std::shared_ptr````) can be used to allow clients to mutually guarantee the lifetime of a single instance.

````c++
class VShared {
    std::shared_ptr<vector<int>> v_;
public:
    VShared() : v_(make_shared(vector<int>(1, 42))) {}
    std::shared_ptr<vector<int>> get_v() { return v_; }
    };

std::shared_ptr<vector<int>> copy;

{
    VShared orig;

    // Assignent operator increments reference count, so the vector
    // remains after orig goes after scope
    copy = orig.get_v();
}

std::cout << *copy[0] << std::endl;
````

# Weak pointers

The above example will persist the vector until the VShared object is deleted.  In some cases that may be an undesirable use of resources, and one might prefer to release the object if no clients are actively using it while still avoiding having multiple instances created at the same time.  Weak pointers (````std::weak_ptr````) allow safe access to objects managed by ````std::shared_ptr```` without participating in the lifetime of the object.

````c++
class VCached {
    std::weak_ptr<vector<int>> v_;
public:
    std::shared_ptr<vector<int>> get_v() {
        if (v_.???) {
        return ???;
        }
        auto v = std::make_shared(std::vector<int>(1, 42));
        v_ = ???
        return v;
    }
};
````

Note that the nature of weak pointers is that the object they point to may not exist.  The benefit they have over raw pointers is that attempting to use them after the underlying object has been freed leads to an exception as opposed to accessing memory inappropriately.

[//]: # Footnotes

[^1]: There is an important technical caveat to this statement, however.  The smart pointers themselves must be copied, not the contents of the smart     pointer.
    For example, this works
    ````c++
    std::weak_ptr<int> copy;
    {
        std::weak_ptr<int> orig = std::make_shared(new int(42));

        // Assignment operator increments the reference count
        copy = orig;

        // When orig goes out of scope, the reference count is still > 0 so the memory is not freed
    }
    std::cout << *copy << endl;
    ````
    But this doesn't
    ````c++
    std::weak_ptr<int> copy;
    {
        std::weak_ptr<int> orig = std::make_shared(new int(42));

        // The reference count never gets updated
        copy.set(orig.get());

        // When orig goes out of scope, the memory is freed
    }

    // Now copy points to freed memory
    std::cout << *copy << endl;
    ````

[^2]: std::vector<int> is being used here for illustration.  I typically run in to this problem with complex objects that require a lot of context to initialize, but can then be used after initialization by different clients.
    
