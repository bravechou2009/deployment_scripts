#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import virtualenv_deploy
import os


current_absdir = os.path.split(os.path.abspath(__file__))[0]


def main():
    sudo('pip install supervisor')
    put(os.path.join(current_absdir, 'config', 'supervisord.conf'), '/etc/supervisord.conf', use_sudo=True)



if __name__ == '__main__':
    fab_prompt.prompt()
    main()
    sys.exit()
