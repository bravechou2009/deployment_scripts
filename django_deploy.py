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

def uwsgi_setup(django_project_name, django_project_dir):
    """set uwsgi up to serve django"""
    sudo('pip install uwsgi')
    uwsgi_ini_file = '/etc/uwsgi/vassals/{0}.ini'.format(django_project_name)
    sudo('mkdir -p /etc/uwsgi/vassals')
    put(os.path.join(current_absdir, 'config', 'uwsgi.ini'), os.path.join('/etc/uwsgi/vassals',
                '{0}.ini'.format(django_project_name)), use_sudo=True)
    sudo('sed -e "s/\*\*USERNAME\*\*/{0}/g" -e "s/\*\*PROJECTNAME\*\*/{1}/g"  -i "/etc/uwsgi/vassals/{1}.ini"'.format(env.user, django_project_name))


def nginx_setup(django_project_name):
    """set up nginx.conf to deal with uwsgi"""
    nginx_conf_loc = '/usr/local/nginx/conf/nginx.conf'
    sudo('touch /usr/local/nginx/conf/nginx.conf')
    sudo('rm {0}'.format(nginx_conf_loc))
    put(os.path.join(current_absdir, 'config', 'nginx.conf'), '/usr/local/nginx/conf/nginx.conf', use_sudo=True)
    sudo('sed -e "s/\*\*USERNAME\*\*/{0}/g" -e "s/\*\*PROJECTNAME\*\*/{1}/g"  -i "/usr/local/nginx/conf/nginx.conf"'.format(env.user, django_project_name))


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
    uwsgi_setup(django_project_name, django_project_dir)
    nginx_setup(django_project_name)


if __name__ == '__main__':
    fab_prompt.prompt()
    virtualenv_deploy.main()
    main()
    sys.exit()
