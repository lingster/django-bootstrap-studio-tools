#!/bin/bash

# this will read all html files and replace dj-* attributes with django code

logfile="/tmp/bss_export.log"
export_script=$(realpath lol.py)

cd $1

# if you have a venv setup, replace the following
source ~/venv/django-bss-tools/bin/activate

echo "run at `date`" >> $logfile
echo "`which python3`" >> $logfile
echo $1 >> $logfile
for f in *.html
do
    echo python3 $cwd/export.py $f >> $logfile 
    python3 $export_script $f 
done
