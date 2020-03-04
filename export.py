import sys
from bs4 import BeautifulSoup

# convert a file from Bootstrap Studio to Django Template

infile = sys.argv[-1]

with open(infile, "r") as fp:
    soup = BeautifulSoup(fp, "lxml")

# handle load
for div in soup.find_all(attrs={"dj-load": True}):
    if div:
        forline = "{% load " + div.get('dj-load') + " %}"
        div.insert_before(forline)
        del div

# handle for
for div in soup.find_all(attrs={"dj-for": True}):
    if div:
        forline = "{% for " + div.get('dj-for') + " %}"
        div.insert_before(forline)
        if 'dj-for' in div.attrs:
            del div.attrs['dj-for']
            div.insert_after('{% endfor %}')

# handle refs
for ref in soup.find_all(attrs={"dj-ref": True}):
    if ref:
        if 'dj-ref' in ref.attrs:
            refattr = ref.get('dj-ref')
            if ref.string:
                ref.string.replace_with('{{ ' + refattr + ' }}')
            del ref.attrs['dj-ref']

# handle if
# eg: <div dj-if="form.errors" >  will get translated to: 
# {% if form.errors %}
# ...
# {% endif %}
for ifs in soup.find_all(attrs={"dj-if": True}):
    if ifs:
        ifline = "{% if " + ifs.get("dj-if") + " %}"
        ifs.insert_before(ifline)
        if "dj-if" in ifs.attrs:
            del ifs.attrs["dj-if"]
            ifs.insert_after("{% endif %}")

# handle block
for div in soup.find_all(attrs={"dj-block": True}):
    if div:
        blockline = "{% block " + div.get('dj-block') + " %}"
        div.insert_before(blockline)
        if 'dj-block' in div.attrs:
            del div.attrs['dj-block']
            div.insert_after('{% endblock %}')
 
# handle scripts,
# eg: <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.js">
# eg <script src="{% static "assets/js/theme.js" %}">
for div in soup.find_all("script"):
    if div:
        if not div.get("src").startswith("http"):
            div.attrs["src"] = "{% static \"" + div.attrs["src"] + "\" %}"""
            
for div in soup.find_all("link"):
    if div:
        if not div.get("href").startswith("http"):
            div.attrs["href"] = "{% static \"" + div.attrs["href"] + "\" %}"""

#print(soup.prettify())
with open(infile, "w") as outfp:
    outfp.write(soup.prettify())
