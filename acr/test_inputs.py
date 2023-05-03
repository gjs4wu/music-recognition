#!/usr/bin/env python3


import os, sys, json
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

config = {
    "host": "identify-us-west-2.acrcloud.com",
    "access_key": "2e1e912234733271cf292651d6519332",
    "access_secret": "yVJNgoJYdVxUwv4a7wW4h4xds1PSjKCdCph1opCv",
    "recognize_type": ACRCloudRecognizeType.ACR_OPT_REC_AUDIO,  # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
    "debug": False,
    "timeout": 15,  # seconds
}

"""This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ..."""
re = ACRCloudRecognizer(config)


def test(path: str, correct_song: str):
    filename = "data/" + path + "/inputs/" + str(i).zfill(4) + ".wav"

    response = re.recognize_by_file(
        filename, 0, ACRCloudRecognizer.get_duration_ms_by_file(filename)
    )
    if type(response) != str:
        return -99, None

    res = json.loads(response)
    if res["status"]["msg"] == "Success":
        song : str = res["metadata"]["music"][0]["title"] 
        if song.find(correct_song) != -1:
            return 1, song
        else:
            return 0, song
    else:
        # print(res)
        return -1, None


num_correct = 0
num_incorrect = 0
num_none = 0

correct: list[int] = []
incorrect: list[int] = []
none: list[int] = []

NUM_TO_TEST = int(sys.argv[2])

for i in range(NUM_TO_TEST):
    res, song_name = test(sys.argv[1], sys.argv[2])
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

results = open("acr/" + sys.argv[1] + "/results.txt", "w")
results.write("Correct\t\t" + str(num_correct) + str(correct) + "\n")
results.write("Incorrect\t" + str(num_incorrect) + str(incorrect) + "\n")
results.write("None\t\t" + str(num_none) + str(none) + "\n")
