#!/usr/bin/env python

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

"""Example script that identifies metadata for files specified on the
command line.
"""
import pyacoustid.acoustid as acoustid 
import sys

API_KEY = 'kkAUAzcqZu'


# Python 2/3 Unicode compatibility: this `print_` function forces a
# unicode string into a byte string for printing on Python 2, avoiding
# errors in the process, and does nothing on Python 3, where
# stdout/stderr are text streams (and there's not much we can do about
# that).
if sys.version_info[0] < 3:
    def print_(s):
        print(s.encode(sys.stdout.encoding, 'replace'))
else:
    def print_(s):
        print(s)


def aidmatch(filename):
    try:
        duration, fp = acoustid.fingerprint_file(filename)
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
        print("none")
        return
    for result in response['results']:
        for recording in result["recordings"]:
            print(recording["title"])


if __name__ == '__main__':
    aidmatch(sys.argv[1])
