import json
import os.path
import shutil
from airium import Airium

allowlist = [".\\.git", ".\\images"]
subfolders = [ f.path for f in os.scandir() if f.is_dir() ]
for sf in subfolders:
    if sf not in allowlist:
        shutil.rmtree(sf)

def createField(Field, Title, Description, Image, URL):
    Field = Field.lower()
    a = Airium()
    a('<!DOCTYPE html>')
    with a.head():
        a.title(_t=Title)
        a.meta(charset='utf-8')
        a.meta(content='Resto Title', property='og:title')
        a.meta(content=Description, property='og:description')
        a.meta(content=URL, property='og:url')
        a.meta(content='https://niseko.github.io/rshaman/images/'+Image, property='og:image')
        a.meta(content='0; URL='+URL, **{'http-equiv': 'refresh'})
        a.meta(content='#43B581', name="theme-color")
        a.link(href=URL, rel='canonical')

    try:
        os.mkdir(Field)
    except Exception:
        pass

    with open(os.path.join(Field, "index.html"), "w") as f:
        f.write(str(a))

with open("fields.json") as file:
    data = json.load(file)

for key in data:
    value = data[key]
    createField(key, value['Title'], value['Description'], value['Image'], value['URL'])
    for syn in value['Synonyms']:
        createField(syn, value['Title'], value['Description'], value['Image'], value['URL'])



    



#print (html)
