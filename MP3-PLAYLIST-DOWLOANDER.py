from pytube import YouTube 
from pytube import Playlist
import os
# where to save
SAVE_PATH = r'C:\Users\E-store\OneDrive\Desktop\Yotube video'
# link of the playlist
playlist_url='https://www.youtube.com/watch?v=h2VaLM85L3g&list=PLRe9ARNnYSY45g8gtWQcC7pNX10TgEUfy'
#giving it a different name
p=Playlist(playlist_url)
#running the videos in the playlist
for video in p:
    try:
        yt = YouTube(video)
    except:
        print("Connection Error") #to handle exception
        
     # filters out all the files with "mp4" extension
    mp3files=  yt.streams.filter(only_audio=True).all()
    try:
        #downloading the video in the prefered folder
        out_file =  mp3files[0].download(output_path=SAVE_PATH)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print(yt.title + " has been successfully downloaded.") 
    except:
        print("Some Error!")
    print('Task Completed!')

