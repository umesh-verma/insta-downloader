import requests

from flask import Flask
url = "https://www.instagram.com/reel/Cp2cSauNGTt/?utm_source=ig_web_copy_link&__a=1&__d=dis"
app = Flask(__name__)



def fileurl(url):
    resp = requests.get(url)
    start = resp.text.find('video_url')+12
    end = resp.text.find('video_view_count')-3
    file = resp.text[start:end]
    return file

file = fileurl(url)
getfile = requests.get(file)

open('abc.mp4','wb').write(getfile.content)

@app.route('/')
def fileurl():
    print(url)
    resp = requests.get(url+'&__a=1&__d=dis')
    start = resp.text.find('video_url')+12
    end = resp.text.find('video_view_count')-3
    file = resp.text[start:end]
    return file