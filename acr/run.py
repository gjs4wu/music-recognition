#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''
    >>> python test.py test.mp3
'''

import json
import os, sys
from acrcloud.recognizer import ACRCloudRecognizer
from acrcloud.recognizer import ACRCloudRecognizeType

if __name__ == '__main__':
    config = {
        'host':'identify-us-west-2.acrcloud.com',
        'access_key':'2e1e912234733271cf292651d6519332',
        'access_secret':'yVJNgoJYdVxUwv4a7wW4h4xds1PSjKCdCph1opCv',
        'recognize_type': ACRCloudRecognizeType.ACR_OPT_REC_AUDIO, # you can replace it with [ACR_OPT_REC_AUDIO,ACR_OPT_REC_HUMMING,ACR_OPT_REC_BOTH], The     SDK decide which type fingerprint to create accordings to "recognize_type".
        'debug':False,
        'timeout':15 # seconds
    }
    
    '''This module can recognize ACRCloud by most of audio/video file. 
        Audio: mp3, wav, m4a, flac, aac, amr, ape, ogg ...
        Video: mp4, mkv, wmv, flv, ts, avi ...'''
    re = ACRCloudRecognizer(config)

    #recognize by file path, and skip 0 seconds from from the beginning of sys.argv[1].
    # print(re.recognize_by_file(sys.argv[1], 0, ACRCloudRecognizer.get_duration_ms_by_file(sys.argv[1])))

    # print("duration_ms=" + str(ACRCloudRecognizer.get_duration_ms_by_file(sys.argv[1])))

    # buf = open(sys.argv[1], 'rb').read()
    #recognize by file_audio_buffer that read from file path, and skip 0 seconds from from the beginning of sys.argv[1].
    # print(re.recognize_by_filebuffer(buf, 0, 10))

    response = re.recognize_by_file(sys.argv[1], 0, ACRCloudRecognizer.get_duration_ms_by_file(sys.argv[1]))
    if type(response) == str:
        res = json.loads(response)
        if(res["status"]["msg"] == "Success"):
            print(res["metadata"]["music"][0]["title"])
        else:
            print(res)
            

