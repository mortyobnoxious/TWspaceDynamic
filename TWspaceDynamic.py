import requests
import time as t
import os

def addToClipBoard(text):
    command = 'echo | set /p nul=' + text.strip() + '| clip'
    os.system(command)

dynamic = str(input("Paste Dynamic URL: "))
master = dynamic.replace('/dynamic_playlist.m3u8?type=live',"/master_playlist.m3u8")

response = requests.get(master)
data = response.text.split('audio-space/')[1].replace(chr(10), "")

play_url = dynamic.replace('dynamic_playlist.m3u8',data).replace('type=live',"type=replay")

addToClipBoard(play_url)
print("Copied to Clipboard, will close in 10 seconds.")
print(play_url)
t.sleep(10)