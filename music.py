# -*- coding: UTF-8 -*-

import json

f=open("files/script.json", "r")
if f.mode == 'r':
    data =f.read()
f.close()

f=open("files/playlist.txt", "a+")

response = json.loads(data)

playlist=response['DATA']['TITLE']

track_number=1
for doc in response['SONGS']['data']:
    content=playlist+"|"+str(track_number)+"|"+doc['ART_NAME']+"|"+doc['SNG_TITLE']+"|"+doc['ALB_TITLE']+"|"+doc['DURATION']+"\n"
    print(content)
    f.write(content)
    track_number += 1
f.close()