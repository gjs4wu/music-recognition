#!/usr/bin/env python3

import asyncio
import sys

from shazamio import Shazam, Serialize

async def main():
  file_name = sys.argv[1]
  
  shazam = Shazam()
  out = await shazam.recognize_song(file_name)
  song_name = Serialize.full_track(out)
  if(song_name.track == None):
    return -1
  print(song_name.track)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())