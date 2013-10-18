#!/usr/bin/env python
from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import virtualenv_deploy
import os


def dep_mount_scripts():
    put('blahblahblah', use_sudo=True)

def main():
    dep_mount_scripts()
    """Deploy backup."""


if __name__ == '__main__':
    fab_prompt.prompt()
    main()
    sys.exit()
