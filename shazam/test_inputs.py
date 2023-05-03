#!/usr/bin/env python3.10

import asyncio
import csv
import sys

from shazamio import Shazam, Serialize


async def test(path: str, correct_song: str):
    filename = "data/" + path + "/inputs/" + str(i).zfill(4) + ".wav"

    shazam = Shazam()
    out = await shazam.recognize_song(filename)
    song_name = Serialize.full_track(out)
    if song_name.track == None:
        return -1, None
    elif song_name.track.title.find(correct_song) != -1 :
        return 1, correct_song
    else:
        return 0, song_name.track.title


num_correct = 0
num_incorrect = 0
num_none = 0

correct : list[int] = []
incorrect : list[int] = []
none : list[int] = []

START = 0
END = 1000

for i in range(START, END):
    res, song_name = asyncio.run(test(sys.argv[1], sys.argv[2]))
    if res == -1:
        print(i, song_name)
        num_none += 1
        none.append(i)
    elif res == 1:
        print(i, song_name)
        num_correct += 1
        correct.append(i)
    elif res == 0:
        print(i, song_name)
        num_incorrect += 1
        incorrect.append(i)

results = open("shazam/" + sys.argv[1] + "_results.txt", "w")
results.write("Correct\t\t" + str(num_correct) + str(correct) + "\n")
results.write("Incorrect\t" + str(num_incorrect) + str(incorrect) + "\n")
results.write("None\t\t" + str(num_none) + str(none) + "\n")