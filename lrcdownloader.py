#!/usr/bin/python

import os
import syncedlyrics
import time
import random
import logging
import argparse

parser = argparse.ArgumentParser(description='Download synced lyrics (.lrc) files for songs')
parser.add_argument('dir', default='.', nargs='?')
parser.add_argument('-r', '--recursive', dest='recoursive', action='store_true', required=False)
args = parser.parse_args()

logging.basicConfig(level=logging.INFO, filename='lrcdownloader.log',
                    filemode='w', format='%(levelname)s %(message)s')


def get_songs(dir, recursive):
    """ return list of songs in the directory, only for audio files,
    songs that already have a .lrc file are omitted"""
    songs = list()
    if recursive:
        for root, dirs, files in os.walk(dir):
            for file in files:
                ext = os.path.splitext(file)[1]         # extension

                if ext == '.mp3' or ext == '.flac':     # audio files
                    song_name = os.path.splitext(file)[0]
                    lrc_file = song_name + '.lrc'
                    lrc_file = os.path.join(root, lrc_file)

                    if not os.path.exists(lrc_file):    # check if lrc file exists
                        songs.append((lrc_file, song_name))
    else:
        for file in os.listdir(dir):
            if os.path.isfile(file):
                ext = os.path.splitext(file)[1]         # extension

                if ext == '.mp3' or ext == '.flac':     # audio files
                    song_name = os.path.splitext(file)[0]
                    lrc_file = song_name + '.lrc'

                    if not os.path.exists(lrc_file):    # check if lrc file exists
                        songs.append((lrc_file, song_name))

    logging.info(f'Songs to get lrc files for:\n{songs}')
    return songs


try:
    dir = os.path.abspath(args.dir)
    logging.info(f'Looking for files in {dir}')

    for song in get_songs(dir, args.recoursive):
        lrc = syncedlyrics.search(song[1])      # get lyrics

        if lrc is not None:
            with open(song[0], 'w') as outfile: outfile.write(lrc)
            logging.info(f'lyrics written for {song[1]}')

        else:
            logging.error(f'{song[1]}, returned {lrc}')

        time.sleep(random.randrange(10, 100)/20)

except Exception as e:
    logging.exception(f'An error occurred while running the script: {str(e)}')
