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
    sudo('rm -rf ~/ffmpeg_build ~/bin/{ffmpeg,ffprobe,ffserver,vsyasm,x264,yasm,ytasm}')
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get -y install build-essential')
    sudo('apt-get -y install build-essential autoconf automake git \
         libass-dev libgpac-dev libsdl1.2-dev libtheora-dev libtool \
         libva-dev libvdpau-dev libvorbis-dev libx11-dev libxext-dev \
         libxfixes-dev pkg-config texi2html zlib1g-dev')

    # H.264 video encoder.
    with cd('~/ffmpeg_sources/x264/'):
        run('make distclean')
        run('git pull')
        run('./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" --enable-static')
        run('make')
        run('make install')

    # AAC audio encoder.
    with cd('~/ffmpeg_sources/fdk-aac/'):
        run('git pull')
        run('autoreconf -fiv')
        run('./configure --prefix="$HOME/ffmpeg_build" --disable-shared')
        run('make')
        run('make install')

    # VP8/VP9 video encoder and decoder.
    with cd('~/ffmpeg_sources/libvpx/'):
        run('make clean')
        run('git pull')
        run('./configure --prefix="$HOME/ffmpeg_build" --disable-examples')
        run('make')
        run('make install')

    # FFMPEG
    with cd('~/ffmpeg_sources/ffmpeg/'):
        run('git pull')
        run('PKG_CONFIG_PATH="$HOME/ffmpeg_build/lib/pkgconfig"')
        run('export PKG_CONFIG_PATH')
        run('./configure --prefix="$HOME/ffmpeg_build" \
            --extra-cflags="-I$HOME/ffmpeg_build/include" \
            --extra-ldflags="-L$HOME/ffmpeg_build/lib" \
            --bindir="$HOME/bin" --extra-libs="-ldl" --enable-gpl \
            --enable-libass --enable-libfdk-aac --enable-libmp3lame \
            --enable-libtheora --enable-libvorbis \
            --enable-libvpx --enable-libx264 --enable-nonfree')
        # not enabling libopus
        # --enable-libopus
        run('make')
        run('make install')
        run('hash -r')


    sys.exit()



if __name__ == '__main__':
   fab_prompt.prompt()
   main()
