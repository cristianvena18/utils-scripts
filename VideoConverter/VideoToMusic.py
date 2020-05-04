import os
import moviepy.editor


def convert(vid, i):
    global path_of_videos
    vid = path_of_videos + '\\' + vid
    print("in convert function ", vid)
    video = moviepy.editor.VideoFileClip(vid)
    audio = video.audio
    audio.write_audiofile(f"path_to_save_audio{i}.mp3")


path_of_videos = input('Entry path to find videos: ')

videos = os.listdir(path_of_videos)
print(videos)
i = 0

for vid in videos:
    if vid.endswith('.mp4'):
        print(f"{i}: {vid} \n")
        convert(vid, i)
        i += 1
