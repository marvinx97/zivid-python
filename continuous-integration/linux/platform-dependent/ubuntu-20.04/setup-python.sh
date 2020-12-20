#!/bin/bash

# Default Python3 installation
apt-get --yes update || exit $?
apt-get --yes install python3 python3-pip || exit $?
update-alternatives --install /usr/bin/python python /usr/bin/python3 0 || exit $?
update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 0 || exit $?
