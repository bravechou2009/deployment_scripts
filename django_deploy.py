#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import virtualenv_deploy

def main():
    """Deploy Django inside a virtual environment."""
    django_project_name = raw_input('Django project name: ')
    run('mkvirtualenv {0}-env'.format(django_project_name))
    with cd('/home/{0}/.virtualenvs/{1}-env'.format(env.user, django_project_name)):
        run('pip install django south django-jenkins')
        run('django-admin.py startproject {0}'.format(django_project_name))
    with cd('/home/{0}/.virtualenvs/{1}-env/{1}'.format(env.user, django_project_name)):
        sudo'chmod +x admin.py')
    sys.exit()




if __name__ == '__main__':
    virtualenv_deploy.main()
    fab_prompt.prompt()
    main()
