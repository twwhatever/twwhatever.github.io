Title: Setting up AWS EC2 instances for system design
Date: 2022-01-20 16:00
Category: Ops
Tags: AWS, Python, NGINX
Slug: aws-ec2-setup
Authors: Ted Wild
Summary: Getting an EC2 instance set up for messing around with Python system design

I found a bunch of system design learning material fairly abstract, which makes me feel less confident.  The goal is to make things more concrete by setting up some of the problems and playing around with the implementations.  The result's obviously not going to be production grade, but it should be enough to gain some confidence in some specific points.

One of the neat things about the modern cloud providers is that you can play around with large scale systems directly.  It seems to me like it should be possible to set up a playground that lets you dig in to real design issues to the depth you want.  You can configure provided pieces at a high level, and drill in to the specific components to whatever level of detail you want.

# Running a Python webserver

These instructions are to get the [Tornado](https://www.tornadoweb.org/en/stable/) server running and accessible on an EC2 instance.  The idea isn't to demonstrate brilliant use of AWS capabilities at this point, but to get something very basic set up so that you can iterate on it.

## Configuring an EC2 instance

More or less [any tutorial](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html) for getting an EC2 instance set up and connected should work.  When setting up the security groups, make sure to allow SSH, HTTP and HTTPS inbound traffic (by default, I think you only get SSH).

Make sure to download the `.pem` file so you can connect to your instance.  I needed to update the permissions to get it to work, for example
```
chmod 400 ~/Downloads/key.pem
ssh -i ~/Downloads/key.pem ec2-user@public-dns
```
Note that you may want to store the key somewhere more durable.  I don't really care too much, since these are temporary machines for me to mess around with.

## Setting up NGINX

By default, the inbound HTTP rule only opens up port 80.  Applications run without sudo won't have access to that port.  You can obviously just run everything via sudo, but it's easy enough to use NGINX to forward traffic from port 80 to any other port you want.

Install and start NGINX:
```
sudo amazon-linux-extras install nginx1
sudo systemctl start nginx.service
```
You should now see the NGINX test page when you open the URL for your EC2 instance.  You can then configure it by editing `/etc/nginx/nginx.conf` and restarting NGINX with `sudo nginx -s reload`.  [This tutorial](https://gist.github.com/soheilhy/8b94347ff8336d971ad0) has a bunch of good basics for NGINX forwarding rules.  In this case, we can forward requests for a given path to a Tornado service that we'll set up.  Add the following to the `server` section:
```nginx
	location /test {
        rewrite ^/test(.*) /$1 break;
	    proxy_pass http://127.0.0.1:8888;
	}
```

## Running the server

Now we can start up the Python server.  `pip3 install tornado`, then copy the [hello, world](https://www.tornadoweb.org/en/stable/#hello-world) sample code in to a file `hello_world.py`.  Finish off with a strong `python3 hello_world.py`, and you should be able to open `http://public-ip/test` and marvel at your results.
