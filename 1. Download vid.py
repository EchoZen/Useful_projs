import requests, os
os.chdir(r'C:\Users\zchen\Documents')
chunksize= 256

url='src="https://www.youtube.com/d8072100-a6ae-42bb-9575-4bbfa74f6a26"></video>'
url= url.replace('"','')
url= url.split('src=')[1].split('></video')[0]

r= requests.get(url, stream= True)
with open('aot1.mp4','wb') as f:
    for chunk in r.iter_content(chunk_size=chunksize):
        f.write(chunk)

