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
    """This function installs various useful linux utilities on a fresh install
    of Debian.
    REF:http://ffmpeg.org/trac/ffmpeg/wiki/UbuntuCompilationGuide"""

    # dependencies:
    sudo('rm -rf ~/ffmpeg_build ~/ffmpeg_sources ~/bin/{ffmpeg,ffprobe,ffserver,vsyasm,x264,yasm,ytasm}')
    sudo('apt-get -y install build-essential')
    sudo('apt-get -y autoremove libass-dev libgpac-dev libsdl1.2-dev libtheora-dev \
         libva-dev libvdpau-dev libvorbis-dev libx11-dev libxext-dev \
         libxfixes-dev pkg-config texi2html zlib1g-dev')
    run('mkdir -p ~/ffmpeg_sources')

    sys.exit()



if __name__ == '__main__':
   fab_prompt.prompt()
   main()
