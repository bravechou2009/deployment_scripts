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
    sudo('apt-get install python-dev libcurl4-gnutls-dev libexpat1-dev \
         gettext libz-dev libssl-dev python-pip git build-essential vim \
         exuberant-ctags autoconf automake git \
         libass-dev libgpac-dev libsdl1.2-dev libtheora-dev libtool \
         libva-dev libvdpau-dev libvorbis-dev libx11-dev libxext-dev \
         libxfixes-dev pkg-config texi2html zlib1g-dev -y')
    sys.exit()









if __name__ == '__main__':
  #  env.user = raw_input('Username: ')
 #   env.host_string = raw_input('Hostname: ')
#    env.password = getpass()
   fab_prompt.prompt()
   main()
