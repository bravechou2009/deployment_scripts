#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import re

def main():
    """Deploy and configure virtualenv and its wrapper."""

    sudo('pip install virtualenv virtualenvwrapper')
    run('export WORKON_HOME=~/envs')
    run('mkdir -p ~/envs')
    try:
        write_bashrc = True
        get('~/.bashrc','/tmp/.bashrc')
        check_file = open('/tmp/.bashrc','r')
        for line in check_file:
            if re.search('source /usr/local/bin/virtualenvwrapper.sh', line):
                write_bashrc = False
            else:
                pass
        check_file.close()
        if write_bashrc:
            run("echo 'source /usr/local/bin/virtualenvwrapper.sh' >> ~/.bashrc")
    except:
        raise
    sys.exit()




if __name__ == '__main__':
   fab_prompt.prompt()
   main()
