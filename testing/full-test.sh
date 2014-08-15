#! /bin/bash

set -e

cd "`dirname $0`/../"

if [[ $1 == "" ]]; then
    echo "This script is designed to be ran when creating packages, it shouldn't normally be ran by end users"
    exit 1
fi

export name="$1"
export category="$2"
export testconfig="$5"

ls -al /usr/share/libvirt-wakeonlan
py.test2 -rxs --cov-report xml  --cov . || py.test -rxs --cov-report xml  --cov .

# start and stop daemon

# gentoo
if [[ -f /etc/gentoo-release ]] ; then
            /etc/init.d/libvirt-wakeonlan status
fi

# redhat
if [[ -f /etc/redhat-release ]] ; then
            service libvirt-wakeonlan status
fi

# debian
if [[ -f /etc/debian-release || -f /etc/debian_version ]] ; then
            service libvirt-wakeonlan status
fi

# arch
if [[ -f /etc/arch-release ]] ; then
            systemctl status libvirt-wakeonlan
fi

exit 0