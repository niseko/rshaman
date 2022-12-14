import json
import os.path
import shutil
from airium import Airium

with open("fields.json") as file:
    data = json.load(file)

# this won't clean up anything
# deleted from the list, but
# it also doesn't delete random stuff
for key in data:
    shutil.rmtree(key, 1)

def createField(Field, Title, Description, URL):
    Field = Field.lower()
    a = Airium()
    a('<!DOCTYPE html>')
    with a.head():
        a.title(_t=Title)
        a.meta(charset='utf-8')
        a.meta(property='og:title', content=Title)
        a.meta(property='og:description', content=Description)
        a.meta(property="og:site_name", content=URL)
        a.meta(property='og:url', content=URL)
        a.meta(property='og:image', content='https://niseko.github.io/rshaman/images/aglogo.png')
        a.meta(content='0; URL='+URL, **{'http-equiv': 'refresh'})
        a.meta(content='#0070DD', name="theme-color")
        #a.meta(name="twitter:card", content="summary_large_image")
        a.link(href=URL, rel='canonical')

    try:
        os.mkdir(Field)
    except Exception:
        pass

    with open(os.path.join(Field, "index.html"), "w") as f:
        f.write(str(a))

for key in data:
    value = data[key]
    createField(key, value['Title'], value['Description'], value['URL'])
    for syn in value['Synonyms']:
        createField(syn, value['Title'], value['Description'], value['URL'])

# Create an overview of all available links
a = Airium()
a('<!DOCTYPE html>')
with a.head():
    a.title(_t="rshaman.com")
    a.meta(charset='utf-8')
    a.meta(property='og:title', content="Overview")
    a.meta(property='og:description', content="A list of available forwardings.")
    a.meta(property="og:site_name", content="rshaman.com")
    a.meta(property='og:url', content="rshaman.com")
    a.meta(property='og:image', content='https://niseko.github.io/rshaman/images/aglogo.png')
    a.meta(content='#0070DD', name="theme-color")
    a.link(href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css", rel="stylesheet", integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx", crossorigin="anonymous")
with a.body():
    with a.div(klass="container"):
        with a.h1():
            a("Overview")
        with a.ul():
            for key in data:
                value = data[key]
                with a.li():
                    a(key)
                    with a.ul():
                        with a.li():
                            with a.a(href=value['URL']):
                                a(value['Title'])
                        with a.li():
                            a("Description: " + value["Description"])

with open("index.html", "w") as f:
    f.write(str(a))