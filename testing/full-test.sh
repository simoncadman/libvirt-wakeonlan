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
exit 0

# gentoo
if [[ -f /etc/gentoo-release ]] ; then
            /etc/init.d/libvirt-wakeonlan start
            /etc/init.d/libvirt-wakeonlan stop
fi

# redhat
if [[ -f /etc/redhat-release ]] ; then
            service libvirt-wakeonlan start
            service libvirt-wakeonlan stop
fi

# debian
if [[ -f /etc/debian-release || -f /etc/debian_version ]] ; then
            service libvirt-wakeonlan start
            service libvirt-wakeonlan stop
fi

# arch
if [[ -f /etc/arch-release ]] ; then
            systemctl start libvirt-wakeonlan
            systemctl stop libvirt-wakeonlan
fi

exit 0