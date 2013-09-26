#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import os


def main():
    """Deploy Django inside a virtual environment."""
    env.shell = "/bin/bash -l -i -c"
    django_project_name = raw_input('Django project name: ')
    sudo('wget -q -O - http://pkg.jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -'
    with cd('/home/{0}/.virtualenvs/{1}-env'.format(env.user, django_project_name)):
        run(workon_virtual_env + 'pip install django south django-jenkins uwsgi')
        run(workon_virtual_env + 'django-admin.py startproject {0}'.format(django_project_name))
    django_project_dir = '/home/{0}/.virtualenvs/{1}-env/{1}'.format(env.user, django_project_name)
    with cd(django_project_dir):
        sudo('chmod +x manage.py')
    uwsgi_setup(django_project_name, django_project_dir)
    nginx_setup(django_project_name)


if __name__ == '__main__':
    fab_prompt.prompt()
    main()
    sys.exit()
