# django-bootstrap-studio-tools
A collection of scripts/tools to help export from Bootstrap Studio(BSS) to django template format

Prerequistes
------------
Install beautifulSoup 4, see: https://www.crummy.com/software/BeautifulSoup/bs4/doc/

or in Ubuntu:
sudo apt-get install python3-bs4

To run:

python export.py <name of your file to convert>

Currently supports following attributes for django conversion:

dj-for   => will create a for loop
dj-refs  => will create ref to variable
dj-if    => will create if block


TODO:
=====
Add automated test to verify code is working. See the example.html and expected.html files. 


