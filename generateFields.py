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
    if not Image:
        Image = "aglogo.png"
    a = Airium()
    a('<!DOCTYPE html>')
    with a.head():
        a.title(_t=Title)
        a.meta(charset='utf-8')
        a.meta(property='og:title', content=Title)
        a.meta(property='og:description', content=Description)
        a.meta(property="og:site_name", content=URL) #rshaman.com
        a.meta(property='og:url', content=URL)
        a.meta(property='og:image', content='https://niseko.github.io/rshaman/images/'+Image)
        a.meta(content='0; URL='+URL, **{'http-equiv': 'refresh'})
        a.meta(content='#43B581', name="theme-color")
        #a.meta(name="twitter:card", content="summary_large_image")
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
