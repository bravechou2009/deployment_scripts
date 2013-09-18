#!/usr/bin/env python

from fabric.api import env
from getpass import getpass
from time import sleep

def prompt():
    """This function installs various useful linux utilities on a fresh install
    of Debian."""
    env.user = raw_input('Username: ')
    env.host_string = raw_input('Hostname: ')
    env.password = getpass()
    sleep(1)
    return








if __name__ == '__main__':
    env.user = raw_input('Username: ')
    env.host_string = raw_input('Hostname: ')
    env.password = getpass()
