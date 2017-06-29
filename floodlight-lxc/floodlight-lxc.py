#!/usr/bin/python3

import lxc
import sys
import os

if not os.geteuid() == 0:
    print("The use of overlayfs requires privileged containers.")
    sys.exit(1)

# Setup the container object
c = lxc.Container("floodlight-lxc")
if not c.defined:
    c.create("download", lxc.LXC_CREATE_QUIET, {"dist": "ubuntu",
                                                   "release": "xenial",
                                                   "arch": "amd64"})
    c.start()
    c.get_ips(timeout=30)
    c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    # c.attach_wait(lxc.attach_run_command, ["apt-get", "dist-upgrade", "-y"])
    # c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "software-properties-common", "-y", "--force-yes"])
    c.attach_wait(lxc.attach_run_command, ["add-apt-repository", "ppa:webupd8team/java", "-y"])
    c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    # c.attach_wait(lxc.attach_run_command, ["apt-get", "install", "oracle-java8-set-default", "-y"])
    # c.attach_wait(lxc.attach_run_command, ["apt-get", "install",
    #                                          "build-essential", "ant", "maven", "python-dev", "git","--force-yes"])
    
    # c.attach_wait(lxc.attach_run_command, ["git", "clone", "git://github.com/floodlight/floodlight.git"])
    # c.attach_wait(lxc.attach_run_command, ["cd", "floodlight/"])
    # c.attach_wait(lxc.attach_run_command, ["git", "submodule", "init"])
    # c.attach_wait(lxc.attach_run_command, ["git", "submodule", "update"])
    # c.attach_wait(lxc.attach_run_command, ["ant"])
    
    # c.attach_wait(lxc.attach_run_command, ["mkdir", "-p", "/var/lib/floodlight"])
    # c.attach_wait(lxc.attach_run_command, ["chmod", "777", "/var/lib/floodlight"])
    
    # c.attach_wait(lxc.attach_run_command, ["java", "-jar", "target/floodlight.jar"])



    c.start()
    c.get_ips(timeout=30)


if not c.start():
    print("Failed to start the container", file=sys.stderr)
    sys.exit(1)

# Query some information
print("Container state: %s" % c.state)
print("Container PID: %s" % c.init_pid)

# Stop the container
if not c.shutdown(30):
    print("Failed to cleanly shutdown the container, forcing.")
    if not c.stop():
        print("Failed to kill the container", file=sys.stderr)
        sys.exit(1)

# Destroy the container
if not c.destroy():
    print("Failed to destroy the container.", file=sys.stderr)
    sys.exit(1)
