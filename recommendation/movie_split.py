from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

video_file = "/home/felipelx/Downloads/assets/noTimeToDie7200-10800.mp4"
with open("time.txt") as f:
    times = f.readlines()

times = [x.strip() for x in times]

for time in times:
    starttime = int(time.split("-")[0])
    endtime = int(time.split("-")[1])
    ffmpeg_extract_subclip(video_file, starttime, endtime, targetname="noTimeToDie"+time+".mp4")
