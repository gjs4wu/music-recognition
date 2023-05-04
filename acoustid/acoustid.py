#!/usr/bin/env python

import requests

# url = "https://api.acoustid.org/v2/lookup"
url = "https://api.acoustid.org/v2/submit"
# url = "https://api.acoustid.org/v2/submission_status"
# url = "https://api.acoustid.org/v2/track/list_by_mbid"

data = {
    "client": "kkAUAzcqZu",
    # "user": "kkAUAzcqZu",
    "duration": "15",
    "fingerprint": "AQAAZImiLUwkBT16wdeFLpaFPMGPZg96HQ8aPaj74MqOHn_g-eh61A-UJ0pKsOKxwzg68cd_HM2JvuGQPA_y_Gjqo1-K79mQIH_gZeEo4XpC7BT85HiFI3mGnPnR48zwHFvjoVaIY89FsA0r7C-uoPzhC8f3oXmGKx-eLEIfD467I_yg64WeKA_24frxLIf8INTRHHx-PDiOQ9-HP_gP5jUOXwfroXyQ5MiLT0d_HCcPX-ilQz8e_PDL5PgxFomWIj8AbYwgiAkjyAFEKgOYckQBUQgRCCFglALCEWOEZMAZIhwQRGDmCVzACQUAaNJQgogUBAkCBBCEECgCIQRcSoRiChgjoJBCAEIUUEAYIZQiRAGBFBMA", 
    # "mbid": "aeb30516-e727-4068-9c91-08532b827e87",
    # "meta" : ["recordings", "usermeta"]
    # "track": "Suite bergamasque : III. Clair de lune",
    # "artist": "Claude Debussy",
}

data = {
    "client": "kkAUAzcqZu",
    "user": "kkAUAzcqZu",
    "id": "676397147",
}

response = requests.post(url, params=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
