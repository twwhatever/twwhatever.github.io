Title: gRPC layout for Python
Date: 2019-03-30 20:30
Category: Tips
Tags: gRPC, Python
Slug: grpc-python
Authors: Ted Wild
Summary: Setting up a layout for gRPC files that works seamlessly with Python

I recently ran in to a minor issue using gRPC in Python.  It turns out
that there are constraints on the .proto directory structure if you
want to build a Python package out of multiple .proto files.  This
constraint doesn't appear to affect the Maven or NuGet plugins, which
caused me to waste a bunch of time since I got those working first and
assumed that other language plugins would be the same.  The issue and solution are
described in detail in this
[GitHub issue](https://github.com/protocolbuffers/protobuf/issues/1491).
In the following, I'll go over an example that reproduces my initial
mistake and a fixed version.

The gRPC developers in the GitHub issue recommend keeping
all the protobuf definitions for a package in a single file.  In that
case, you won't have this problem at all.  However, the workaround
presented here is not onerous, especially if followed from the start.

For concreteness, there is a
[simple demo](https://github.com/twwhatever/demo-grpc-python) that
illustrates both the incorrect and working structures.

The initial setup I had was the following directory structure

* proto/
    * message.proto
    * service.proto
* demo/
    * demo.py

With message.proto

````proto
syntax = "proto3";
package twwhatever.demo;
message DemoMessage {
    string m = 1;
}
````

and service.proto
````proto
syntax = "proto3";
package twwhatever.demo;
import "message.proto";
service DemoService {
    rpc Function (DemoMessage) returns (DemoMessage) {}
}
````

My plan was to generate the Python bindings using the following
command in the demo directory via 

````
python -m grpc_tools.protoc \
    -I../proto-wrong/ \
    --python_out=twwhatever/demo \
    --grpc_python_out=twwhatever/demo \
    ../proto-wrong/*.proto
````

That command succeeded and generates the bindings as expected.  When I
tried to create a service, though, I got an error.

````python
from twwhatever.demo import service_pb2_grpc
from twwhatever.demo import message_pb2

class Demo(service_pb2_grpc.DemoServiceServicer):
    def Function(self, request, context):
        return message_pb2.DemoMessage(m='Hi there!')

if __name__ == '__main__':
    demo = Demo()
    print(demo.Function(None, None))
````

Unfortunately, importing the definitions in service.proto doesn't
work because the generated code service_pb2_grpc.proto contains the statement

````python
import message_pb2 as message__pb2
````

which doesn't work because message_pb2 is actually in the twwhatever.demo module.

There appear to be a couple workarounds:
* Keep all the protocol buffer definitions you need in a single file
* Mirror the directory structure of your protocol buffer definitions - in particular your import statements - with your target Python package

In this case, it meant setting up the repository like this

* proto/twwhatever/demo/
    * message.proto
    * service.proto
* demo/
    * demo.py

Changing the import statement in service.proto to

````proto
import "twwhatever/demo/message.proto" 
````

And invoking the command from the Python directory like

````
python -m grpc_tools.protoc \
    -I../proto/ \
    --python_out=. \
    --grpc_python_out=. \
    ../proto/twwhatever/demo/*.proto
````

That way I got a package twwhatever.demo and I could use

````python
from twwhatever.demo import service_pb2_grpc
from twwhatever.demo import message_pb2
````

It appears that the same strategy works if you add
additional submodule structure (e.g., twwhatever/demo/mypackage, etc.).

The takeaway seems to be to put all the protocol buffer definitions
for a project under the same directory structure, and possibly better
yet in the same .proto file.
