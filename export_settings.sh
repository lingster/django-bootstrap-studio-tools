#!/bin/bash

# this will read all html files and replace dj-* attributes with django code
# YOU MAY NEED TO copy the python export.py script to the same folder as where BSS app image is located

logfile="/tmp/bss_export.log"
cwd=`pwd`

# if you have a venv setup, replace the following
source ~/venv/django-bss-tools/bin/activate

echo "run at `date`" >> $logfile
echo "`which python3`" >> $logfile
echo $cwd >> $logfile
echo $1 >> $logfile
pushd $1
for f in *.html
do
    echo python3 $cwd/export.py $f >> $logfile 
    python3 $cwd/export.py $f 
done
popd

