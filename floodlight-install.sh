#!/bin/bash

if [ `id -u` -ne '0' ]; then
  echo "This script must be run as root" >&2
  exit 1
fi

echo "Installing recommends applications..."

if ! hash build-essential ant maven python-dev git software-properties-common python-software-properties 2>/dev/null; then
    apt-get -y install build-essential ant maven python-dev git software-properties-common python-software-properties
else
    echo "Recommends applications already installed";
fi

echo "Installing Java 8..."
add-apt-repository ppa:webupd8team/java
apt-get update
sudo apt-get install -y oracle-java8-set-default

echo "Downloading depends..."0
git clone git://github.com/floodlight/floodlight.git
cd floodlight
git submodule init
git submodule update
ant

mkdir /var/lib/floodlight
chmod 777 /var/lib/floodlight
