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
    c.create("download", lxc.LXC_CREATE_QUIET, {"dist": "debian",
                                                   "release": "jessie",
                                                   "arch": "amd64"})
    c.start()
    c.get_ips(timeout=30)
    c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    c.attach_wait(lxc.attach_run_command, ["apt-get", "dist-upgrade", "-y"])

    c.start()
    c.get_ips(timeout=30)
    c.attach_wait(lxc.attach_run_command, ["apt-key", "adv", "--keyserver", "hkp://keyserver.ubuntu.com:80", "--recv-keys", "EEA14886"])
    c.attach_wait(lxc.attach_run_command, ["apt-get", "update"])
    c.attach_wait(lxc.attach_run_command, ["apt-get", "install",
                                             "build-essential", "ant", "mave", "python-dev", "oracle-java8-installer" , "git", "-y"])

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
