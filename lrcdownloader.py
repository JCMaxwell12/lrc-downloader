#!/usr/bin/python

import os
import syncedlyrics
import time
import random
import logging

logging.basicConfig(level=logging.INFO,
                    filename='lrcdownloader.log')

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
    logging.info(f'Songs to get lrc files for:\n{songs}')
    return songs


for song in get_songs(dir):
    lrc = syncedlyrics.search(song[1])      # get lyrics

    if lrc is not None:
        with open(song[0], 'w') as outfile:
            outfile.write(lrc)
        logging.info(f'lyrics written for {song[1]}')

    else:
        logging.error(f'{song[1]}, returned {lrc}')

    time.sleep(random.randrange(10, 100)/20)
