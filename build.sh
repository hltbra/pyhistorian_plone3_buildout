#!/bin/bash
HERE=$(dirname $0)
buildout_dir=$(readlink -f $HERE)
cd "$buildout_dir"/src

if [ -e "pyhistorian" ]; then
    cd pyhistorian
    git pull origin plone3
else
    git clone https://github.com/hugobr/pyhistorian.git
    cd pyhistorian
    git checkout -b plone3 origin/plone3
fi

cd "$buildout_dir"
bin/buildout
