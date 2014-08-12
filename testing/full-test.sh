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

exit 0