from pydub import AudioSegment
import os
import numpy as np
from pydub.utils import mediainfo

StrtMin = 0
StrtSec = 35
EndMin = 0
EndSec = 45

StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

input_files_list = os.listdir('.\\in\\')
for input_file in input_files_list:
    original_bitrate = mediainfo('.\\in\\{}'.format(input_file))['bit_rate']
    song_sound = AudioSegment.from_file('.\\in\\{}'.format(input_file))
    tag_sound = AudioSegment.from_file('tag.mp3', format='mp3')
    extract = song_sound[StrtTime:EndTime]

    overlay = extract.overlay(tag_sound + 4, position=0)
    
    overlay.export('.\\out\\{}_SNIPPET.mp3'.format(input_file), format='mp3', bitrate=original_bitrate)
