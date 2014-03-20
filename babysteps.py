#!/usr/bin/env python

from __future__ import with_statement
from fabric.contrib.console import confirm
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env)
from fabric.contrib.console import confirm
from getpass import getpass
import cmd
import sys
import fab_prompt

def main():
    """This function installs various useful linux utilities on a fresh install
    of Debian."""

    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get -y install build-essential')
    run('gcc -v')
    run('make -v')
    sudo('apt-get -y install python-dev libcurl4-gnutls-dev libexpat1-dev \
         gettext libz-dev libssl-dev python-pip git build-essential vim \
         exuberant-ctags autoconf automake git smartmontools gsmartcontrol')
    sys.exit()









if __name__ == '__main__':
   fab_prompt.prompt()
   main()
