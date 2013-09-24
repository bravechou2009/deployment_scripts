#!/usr/bin/env python

from __future__ import with_statement
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
import sys
import fab_prompt
import virtualenv_deploy
import os

def main():
    """Deploy Django inside a virtual environment."""
    env.shell = "/bin/bash -l -i -c"
    django_project_name = raw_input('Django project name: ')
    run('mkvirtualenv {0}-env'.format(django_project_name))
    workon_virtual_env = 'workon {0}-env && '.format(django_project_name)
    with cd('/home/{0}/.virtualenvs/{1}-env'.format(env.user, django_project_name)):
        run(workon_virtual_env + 'pip install django south django-jenkins uwsgi')
        run(workon_virtual_env + 'django-admin.py startproject {0}'.format(django_project_name))
    django_project_dir = '/home/{0}/.virtualenvs/{1}-env/{1}'.format(env.user, django_project_name)
    with cd(django_project_dir):
        sudo('chmod +x manage.py')

    sudo('pip install uwsgi')
    uwsgi_ini_file = '/etc/uwsgi/vassals/{0}.ini'.format(django_project_name)
    sudo('mkdir -p /etc/uwsgi/vassals')
    sudo('echo "[uwsgi]" > {0}'.format(uwsgi_ini_file))
    sudo('echo "master = True" >> {0}'.format(uwsgi_ini_file))
    sudo('echo "threads = 2" >> {0}'.format(uwsgi_ini_file))
    sudo('echo "home = {1}" >> {0}'.format(uwsgi_ini_file, django_project_dir))
    sudo('echo "chdir = {1}" >> {0}'.format(uwsgi_ini_file, django_project_dir))
    sudo('echo "socket = /tmp/{1}.sock" >> {0}'.format(uwsgi_ini_file, django_project_name))
    sudo('echo "chmod-socket = 646" >> {0}'.format(uwsgi_ini_file))
    sudo('echo "pythonpath = .." >> {0}'.format(uwsgi_ini_file))
    sudo('echo "env = DJANGO_SETTINGS_MODULE={1}.settings" >> {0}'.format(uwsgi_ini_file, django_project_name))
    sudo('echo "module = {1}.wsgi" >> {0}'.format(uwsgi_ini_file, django_project_name))
    sudo('echo "stats = 127.0.0.1:9191" >> {0}'.format(uwsgi_ini_file))
    sudo('echo "wsgi-file = /home/{1}/.virtualenvs/{2}-env/{2}/{2}/uwsgi.py" >> {0}'.format(uwsgi_ini_file, env.user, django_project_name))
    sudo('echo "virtualenv = /home/{1}/.virtualenvs/{2}-env" >> {0}'.format(uwsgi_ini_file, env.user, django_project_name))


if __name__ == '__main__':
    fab_prompt.prompt()
    virtualenv_deploy.main()
    main()
    sys.exit()
