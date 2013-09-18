#!/usr/bin/env python

from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env)
#from __future__ import with_statement
from fabric.contrib.console import confirm
import sys


def main(args):
    """This function installs various useful linux utilities on a fresh install
    of Debian."""
    if len(args) < 4 or len(args) > 4:
        sys.exit("Please provide username, hostname, and password for remote.")
    else:
        env.user = args[1]
        env.host_string = args[2]
        env.password = args[3]
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get install build-essential -y')
    sudo('apt-get install python-dev libcurl4-gnutls-dev libexpat1-dev gettext \
            libz-dev libssl-dev python-pip git build-essential vim -y')
    run('gcc -v')
    run('make -v')










if __name__ == '__main__':
    main(sys.argv)
