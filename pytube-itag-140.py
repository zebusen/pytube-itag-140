import os.path
import os
os.system('pip install pytube')
import sys
import time
import pytube
from pytube import YouTube
print("YouTube audio downloader using pytube")
url_input = input("Enter YouTube URL: ")
dir_input = input("Enter directory for download: ")
yt = YouTube(url_input)
checker = ''
print(yt.title)
while checker != 'Y' :
    checker = ''
    dilemma = input("Download audio file from this video? (Y/N): ")
    stream = yt.streams.get_by_itag(140)
    if dilemma.upper() == 'Y' :
        print("Downloading " + yt.title)
        checker = 'Y'
        stream.download(dir_input)
        print("Download finished, exiting the program in 5 seconds")
        time.sleep(5)
        sys.exit()
    elif dilemma.upper() == 'N' :
        print("Cancelled downloading " + yt.title + " stopping the program in 5 seconds")
        checker = 'N'
        time.sleep(5)
        sys.exit()
    else :
        print("Please enter only Y for yes and N for no")
        checker = 'N'