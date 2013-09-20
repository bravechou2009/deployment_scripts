#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import virtualenv_deploy

def main():
    """Deploy Django inside a virtual environment."""
    env.shell = "/bin/bash -l -i -c"
    django_project_name = raw_input('Django project name: ')
    run('mkvirtualenv {0}-env'.format(django_project_name))
    workon_virtual_env = 'workon {0}-env && '.format(django_project_name)
    with cd('/home/{0}/.virtualenvs/{1}-env'.format(env.user, django_project_name)):
        run(workon_virtual_env + 'pip install django south django-jenkins')
        run(workon_virtual_env + 'django-admin.py startproject {0}'.format(django_project_name))
    with cd('/home/{0}/.virtualenvs/{1}-env/{1}/'.format(env.user, django_project_name)):
        sudo('chmod +x manage.py')
    sys.exit()




if __name__ == '__main__':
    fab_prompt.prompt()
    virtualenv_deploy.main()
    main()
