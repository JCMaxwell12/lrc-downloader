#!/usr/bin/python

import os
import syncedlyrics
import time
import random

dir = '/home/rhea/Music/'


def get_songs(dir):
    """ return list of songs in the directory, only for audio files,
    songs that already have a .lrc file are omitted"""
    songs = list()
    for root, dirs, files in os.walk(dir):
        for file in files:
            ext = os.path.splitext(file)[1]         # extension

            if ext == '.mp3' or ext == '.flac':     # audio files
                song_name = os.path.splitext(file)[0]
                lrc_file = song_name + '.lrc'
                lrc_file = os.path.join(root, lrc_file)

                if not os.path.exists(lrc_file):    # check if lrc file exists
                    songs.append((lrc_file, song_name))

    return songs


#for song in get_songs(dir):
#    with open(song[0], 'w') as outfile:
#        try:
#            outfile.write(syncedlyrics.search(song[1]))
#            print(song[1])
#        except:
#            print(f'some error ocured with {song[1]}')
#
#        time.sleep(random.randrange(10, 100)/20)
