__author__ = 'stevenL'

import audiotools
import shlex
import subprocess


import os.path

## Encode a .flac (lossless audio file) to AAC in .m4a container

FLAC = 'flac_sample_24bit.flac'
AAC_C = 'aac_test.m4a'


if not os.path.isfile(AAC_C):
    conversion = 'ffmpeg -i flac_sample_24bit.flac -c:a aac -strict experimental %s' % (AAC_C)
    args = shlex.split(conversion)
    subprocess.Popen(args)



##Examine the bitrates from .flac to .aac


audioL = audiotools.open(AAC_C)

print audioL.bits_per_sample()

#print ff.cmd.decode()
