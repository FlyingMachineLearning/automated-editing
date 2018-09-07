"""
Dependencies
"""
import os
from pydub import AudioSegment

"""
pydub has a hard time finding ffmpeg
if there's a workaround, please let me know
"""

AudioSegment.converter = 'D:/ffmpeg.exe'

"""
Where to find the files and where to place them
"""

path1 = '{Path with Assets}'
path2 = '{Output Path}'
end = ".mp3"

"""
Edit this list for your process
"""
listOfAssets = ['intro','bg','outro']

listOfAudio = [AudioSegment.from_mp3(path1+i+end) for i in listOfAssets]
silence = AudioSegment.silent(duration=1000)

folders = [name for name in os.listdir(".") if os.path.isdir(name)]

"""
The loop finds all the folders
  For each file, it creates the eventual name
  The sublist is the list of assets in the folder.
  There's wiggle room for style here.
  My process assumes all finals in alphabetical order.
  You might need RegEx for your process
  It takes the content, 
    puts silence on either side,
    overlays the background,
    fades out the content with overlayed background,
    appends the intro and outro,
    spits out a file.
"""
  
for folder in folders:
    local = path1+folder+"/"
    finalName = {Your code here}
    sublist = sorted(os.listdir(folder))
    topic = AudioSegment.from_mp3(local+sublist[0])
    content = silence + AudioSegment.from_mp3(local+sublist[1]) + silence
    middle = content.overlay(listOfAudio[1], loop=True).fade_out(1000)

    full = listOfAudio[0] + topic + middle + listOfAudio[2]
    full.export(path2+finalName+'.mp3', format="mp3")
