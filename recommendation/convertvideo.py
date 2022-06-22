import os
import subprocess
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

mkv_list = os.listdir("assets")

for mkv in mkv_list:
    ffmpeg -i input.mp4 output.mkv

    output_name = name + ".mp4"
    try:
        subprocess.run(
            ["ffmpeg", "-i", f"assets/{mkv}", "-codec", "copy", f"{output_name}"],
        )
    except:
        raise Exception(f"Error converting {mkv}")
    
