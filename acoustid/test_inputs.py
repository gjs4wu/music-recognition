#!/usr/bin/env python3

# This file is part of pyacoustid.
# Copyright 2011, Adrian Sampson.
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

import sys
import pyacoustid.acoustid as acoustid 

API_KEY = 'kkAUAzcqZu'

if sys.version_info[0] < 3:
    def print_(s):
        print(s.encode(sys.stdout.encoding, 'replace'))
else:
    def print_(s):
        print(s)

def test(path: str, correct_song: str):
    try:
        duration, fp = acoustid.fingerprint_file(path)
        response = acoustid.lookup(API_KEY, fp, duration, meta=['recordings', 'usermeta'])
    except acoustid.NoBackendError:
        print("chromaprint library/tool not found", file=sys.stderr)
        sys.exit(1)
    except acoustid.FingerprintGenerationError:
        print("fingerprint could not be calculated", file=sys.stderr)
        sys.exit(1)
    except acoustid.WebServiceError as exc:
        print("web service request failed:", exc.message, file=sys.stderr)
        sys.exit(1)

    if len(response["results"]) == 0:
        print("None")
        return -1, None
    incorrect = ""
    for result in response['results']:
        for recording in result["recordings"]:
            if recording["title"].find(correct_song) != -1:
                print(recording["title"])
                return 1, correct_song
            else:
                incorrect = recording["title"]
    
    print(incorrect)
    return 0, incorrect


num_correct = 0
num_incorrect = 0
num_none = 0

correct = []
incorrect = []
none = []

NUM_TO_TEST = int(sys.argv[3])

for i in range(NUM_TO_TEST):
    filename = "data/" + sys.argv[1] + "/inputs/" + str(i).zfill(4) + ".wav"

    res, song_name = test(filename, sys.argv[2])
    if res == -1:
        num_none += 1
        none.append(i)
    elif res == 1:
        num_correct += 1
        correct.append(i)
    elif res == 0:
        num_incorrect += 1
        incorrect.append(i)

results = open("acoustid/" + sys.argv[1] + "_results.txt", "w")
results.write("Correct\t\t" + str(num_correct) + str(correct) + "\n")
results.write("Incorrect\t" + str(num_incorrect) + str(incorrect) + "\n")
results.write("None\t\t" + str(num_none) + str(none) + "\n")