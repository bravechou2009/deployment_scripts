#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env)
from fabric.contrib.console import confirm
import sys
import fab_prompt

def main():
    """Deploy and (default) configure supervisord."""

    sudo('pip install supervisor')
    run("echo_supervisord_conf")
    sudo("echo_supervisord_conf > /etc/supervisord.conf")
    sys.exit()




if __name__ == '__main__':
   fab_prompt.prompt()
   main()
