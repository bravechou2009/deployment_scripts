#!/usr/bin/env python

from __future__ import with_statement
from fabric.contrib.console import confirm
from fabric.api import (local, run, sudo, put, get, prompt, reboot, abort,
     settings, env, cd)
from fabric.contrib.console import confirm
from getpass import getpass
import cmd
import sys
import fab_prompt

def main():
    """This function installs nginx on a fresh installi of Debian."""



    # dependencies:
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get install -y libc6 libexpat1 libgd2-xpm libgeoip1 libpam0g \
         libpcre3 libssl1.0.0 libxml2 libxslt1.1 zlib1g libpcre3-dev')
    run('mkdir -p ~/nginx_sources')

    # rtmp module.
    try:
        with cd('~/nginx_sources/'):
            run('git clone --depth 1 git://github.com/arut/nginx-rtmp-module.git')
    except:
        with cd('~/nginx_sources/nginx-rtmp-module/'):
            run('git pull')

    # aws auth module.
    try:
        with cd('~/nginx_sources/'):
            run('git clone --depth 1 git://github.com/anomalizer/ngx_aws_auth.git')
    except:
        with cd('~/nginx_sources/ngx_aws_auth/'):
            run('git pull')

    # nginx
    with cd('~/nginx_sources/'):
        try:
            run('wget http://nginx.org/download/nginx-1.4.1.tar.gz')
            run('tar xzvf nginx-1.4.1.tar.gz')
        except:
            pass
    with cd('/home/{0}/nginx_sources/nginx-1.4.1/'.format(env.user)):
        run('./configure --sbin-path=/usr/local/sbin \
                --with-http_flv_module --with-http_mp4_module \
                --with-http_ssl_module --with-http_secure_link_module \
                --with-http_stub_status_module \
                --with-http_gzip_static_module \
                --add-module=/home/{0}/nginx_sources/nginx-rtmp-module \
                --add-module=/home/{0}/nginx_sources/ngx_aws_auth'.format(env.user))
        run('make')
        # --add-module=~/nginx_sources/nginx-rtmp-module \
        sudo('make install')


    sys.exit()



if __name__ == '__main__':
   fab_prompt.prompt()
   main()
   ffmpeg_update.main()
