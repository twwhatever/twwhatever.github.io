Title: Overview of C++ smart pointers
Date: 2019-02-17 22:40
Category: Tips
Tags: C++
Slug: c++-smart-pointers
Authors: Ted Wild
Summary: Examples of using C++ smart pointers to manage ownership

The problem[^1]:

```c++

std::vector<int>* get_v() {
    return new std::vector<int>(1, 42);
};
```

To ensure there are no memory leaks, the caller must call `delete ` on the
returned pointer.  I'll use a block scope to illustrate, but in general this issue comes in to play when objects with
different lifetimes need access to the same data.

```c++
std::vector<int>* copy;

{
    std::vector<int>* orig = get_v();
    copy = orig;

    // Can't call delete here (unless you copy v)
}

std::cout << *copy[0] << std::endl;

// Have to remember to call delete 
delete copy;
```

A standard approach to the problem is to have an object manage the lifetime of the vector.

```c++
class VOwner {
    std::vector<int> v_;
public:
    VOwner() : v_(1, 42) {}

    // Returning a pointer for consistency, but a reference might be a better idea in practice
    std::vector<int>* get_v() { return v_; }
};
```

In this case, we say that the `VOwner` object *owns* the vector.  While that removes the need to delete the vector, the user must now ensure that the VOwner object has a longer lifetime than any caller of `VOwner::get_v`.

```c++
std::vector<int>* copy;

{
    VOwner orig;
    copy = orig.get_v();
    // Oops, vector gets destroyed when orig goes out of scope
}

// Kaboom
std::cout << (*copy)[0] << std::endl;
```

In many cases the program can be structured so that the owner object
can outlive all of its users.  However, in some cases this structure
can be burdensome if lifetime dependencies are hard to unravel, or worse, fundamentally entangled.

Smart pointers allow safe access to objects on the heap without
coupling the access to the client object lifetime.

# Unique pointers

Unique pointers (`std::unique_ptr`) ensure that an object has exactly one owner.  It is possible to change the owner by moving the unique pointer.  That allows us to safely implement the original example[^2].

```c++
std::unqiue_ptr<vector<int>> get_unique_v() {
    return std::make_unique<vector<int>>(1, 42);
}

std::unique_ptr<std::vector<int>> copy;

{
    std::unique_ptr<std::vector<int>> orig = get_unique_v();
    copy = std::move(orig);
    // Now orig can no longer be used to access the vector
}

std::cout << (*copy)[0] std::endl;

// The vector will be freed when copy goes out of scope, no need to manually call delete
```

# Shared pointers

Another common case is when a single object instance needs to be shared by multiple clients.  This capability is useful when the instance is expensive to construct, for example.  Shared pointers (`std::shared_ptr`) can be used to allow clients to mutually guarantee the lifetime of a single instance.

```c++
class VShared {
    std::shared_ptr<std::vector<int>> v_;
public:
    VShared() : v_(std::make_shared<std::vector<int>>(1, 42)) {}
    std::shared_ptr<std::vector<int>> get_v() { return v_; }
};

std::shared_ptr<std::vector<int>> copy;

{
    VShared orig;

    // Assignent operator increments reference count, so the vector
    // remains after orig goes after scope
    copy = orig.get_v();
}

std::cout << (*copy[0]) << std::endl;
```

# Weak pointers

The above example will persist the vector until the VShared object is
deleted.  In some cases, one might prefer to release the object if no
clients are actively using it, while still avoiding creating multiple
instances if one already exists.  Weak pointers (`std::weak_ptr`) allow safe access to objects managed by `std::shared_ptr` without participating in the lifetime of the object.

```c++
class VCached {
    std::weak_ptr<std::vector<int>> v_;
public:
    std::shared_ptr<std::vector<int>> get_v() {
        auto candidate =  v_.lock();
        if (candidate) {
            return candidate;
        }
        auto v = std::make_shared<std::vector<int>>(1, 42);
        v_ = v;
        return v;
    }
};
```

Note that the nature of weak pointers is that the object they point to
may not exist.  The benefit they have over raw pointers is that
attempting to use them after the underlying object has been freed
leads to a controlled failure.

[//]: # (Footnotes)

[^1]: `std::vector<int>` is being used here for illustration.  I typically run in to this problem with complex objects that require a lot of context to initialize, but can then be used after initialization by different clients.

[^2]: There is an important technical caveat to this statement, however.  The smart pointers themselves must be copied, not the contents of the smart     pointer.
