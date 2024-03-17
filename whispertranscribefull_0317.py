from pytube import YouTube
import ffmpeg
import os.path
import sys
#for concat strings
#MUST HAVE ffmpeg TO WORK
#https://stackoverflow.com/questions/73845566/openai-whisper-filenotfounderror-winerror-2-the-system-cannot-find-the-file
#https://stackoverflow.com/questions/55081352/how-to-convert-mp4-to-mp3-using-python

SAVE_PATH = "C:/Users/Windows/OneDrive/Pictures/"
#STRING_concat
NAME = "tvbs"
VIDEO_path = NAME + ".mp4"
AUDIO_path = NAME + "sound.mp3"


# link of the video to be downloaded
link = "https://www.youtube.com/watch?v=fHJliIxhKe0" #THIS WORKS

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error check wifi")


yt = YouTube(link)
#yt.set_filename('frankensteinvid')

# get the video with the extension and
# resolution passed in the get() function
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    yt.streams.filter(progressive = True,
                      file_extension = "mp4").first().download(output_path = SAVE_PATH,
                                                               filename = VIDEO_path)
    #d_yt.download(SAVE_PATH)
    print("successe")
except:
    print("Youtube Download Error!")
print('Task Completed!')

from moviepy.editor import *
try:
    video = VideoFileClip(os.path.join(SAVE_PATH, VIDEO_path))
    video.audio.write_audiofile(os.path.join(SAVE_PATH, AUDIO_path))
    print("done convert")
except:
    print("Issue with mp4 to mp3")


import whisper
from whisper.utils import get_writer
model = whisper.load_model("medium") #medium small
audio = os.path.join(SAVE_PATH, AUDIO_path)
result = model.transcribe(audio)
#output_directory = os.path.join((SAVE_PATH,"firsttry.txt"))
output_directory = SAVE_PATH

#cn
txt_writer = get_writer("txt", output_directory)
txt_writer(result, audio)
print("still going")
