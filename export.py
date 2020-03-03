import sys
from bs4 import BeautifulSoup

infile = sys.argv[-1]

with open( infile ) as fp:
    soup = BeautifulSoup(fp, "lxml")
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
        if 'dj-ref' in ref.attrs:
            refattr = ref.get('dj-ref')
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


    print (soup.prettify())
