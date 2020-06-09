# django-bootstrap-studio-tools
A collection of scripts/tools to help export from Bootstrap Studio(BSS) to django template format

Prerequistes
------------
Install beautifulSoup 4, see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/ ideally in a virtualenv, 
eg:
```
python -m venv ~/venv/django-bss-tools
source ~/venv/django-bss-tools/bin/activate
python -m pip install pipenv
pipenv install
```

or in Ubuntu:
```
sudo apt-get install python3-bs4
```

To run:

`python export.py <name of your file to convert/process>`

Currently supports following attributes for django conversion:

```
dj-for   => will create a for loop
dj-ref   => will create ref to variable
dj-if    => will create if block
dj-block => will create a block
```

In bootstrap Studio, you can include the script `export_settings.sh` in the advance option in the export settings.
So your html files will automatically be converted into django template format.

If this is not working, you will need to copy the `export.py` script to the location of your BSS app image.

Also you need to ensure that you have BeautifulSoup installed correctly.


TODO:
=====
Add automated test to verify code is working. See the example.html and expected.html files. 


