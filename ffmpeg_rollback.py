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
    sudo('apt-get update -y && apt-get upgrade -y')
    sudo('apt-get -y install build-essential')
    sudo('apt-get -y install build-essential autoconf automake git \
         libass-dev libgpac-dev libsdl1.2-dev libtheora-dev libtool \
         libva-dev libvdpau-dev libvorbis-dev libx11-dev libxext-dev \
         libxfixes-dev pkg-config texi2html zlib1g-dev')
    run('mkdir -p ~/ffmpeg_sources')

    # Yasm is an assembler used by x264 and FFmpeg.
    with cd('~/ffmpeg_sources/'):
        run('wget http://www.tortall.net/projects/yasm/releases/yasm-1.2.0.tar.gz')
        run('tar xzvf yasm-1.2.0.tar.gz')
    with cd('~/ffmpeg_sources/yasm-1.2.0/'):
        run('./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin"')
        run('make')
        run('make install')
        run('make distclean')
        run('. ~/.profile')

    # H.264 video encoder.
    with cd('~/ffmpeg_sources/'):
        try:
            run('git clone --depth 1 git://git.videolan.org/x264.git')
        except:
            pass
    with cd('~/ffmpeg_sources/x264/'):
        run('./configure --prefix="$HOME/ffmpeg_build" --bindir="$HOME/bin" --enable-static')
        run('make')
        run('make install')
        run('make distclean')

    # AAC audio encoder.
    with cd('~/ffmpeg_sources/'):
        try:
            run('git clone --depth 1 git://github.com/mstorsjo/fdk-aac.git')
        except:
            pass
    with cd('~/ffmpeg_sources/fdk-aac/'):
        run('autoreconf -fiv')
        run('./configure --prefix="$HOME/ffmpeg_build" --disable-shared')
        run('make')
        run('make install')
        run('make distclean')

    # MP3 audio encoder.
    with cd('~/ffmpeg_sources/'):
        try:
            run('wget http://downloads.sourceforge.net/project/lame/lame/3.99/lame-3.99.5.tar.gz')
            run('tar xzvf lame-3.99.5.tar.gz')
        except:
            pass
    with cd('~/ffmpeg_sources/lame-3.99.5/'):
        run('./configure --prefix="$HOME/ffmpeg_build" --enable-nasm --disable-shared')
        run('make')
        run('make install')
        run('make distclean')

    '''this is broken
    # Opus audio decoder and encoder.
    with cd('~/ffmpeg_sources/'):
        try:
            run('wget http://downloads.xiph.org/releases/opus/opus-1.0.3.tar.gz')
            run('tar xzvf opus-1.0.3.tar.gz')
        except:
            pass
    with cd('~/ffmpeg_sources/opus-1.0.3/'):
        run('./configure --prefix="$HOME/ffmpeg_build" --disable-shared')
        run('make')
        run('make install')
        run('make distclean')
    '''

    # VP8/VP9 video encoder and decoder.
    with cd('~/ffmpeg_sources/'):
        try:
            run('git clone --depth 1 http://git.chromium.org/webm/libvpx.git')
        except:
            pass
    with cd('~/ffmpeg_sources/libvpx/'):
        run('./configure --prefix="$HOME/ffmpeg_build" --disable-examples')
        run('make')
        run('make install')
        run('make clean')

    # FFMPEG
    with cd('~/ffmpeg_sources/'):
        try:
            run('git clone --depth 1 git://source.ffmpeg.org/ffmpeg')
        except:
            pass
    with cd('~/ffmpeg_sources/ffmpeg/'):
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
        run('make distclean')
        run('hash -r')


    sys.exit()



if __name__ == '__main__':
   fab_prompt.prompt()
   main()
