#!/usr/bin/env python

import requests

url = "https://api.acoustid.org/v2/lookup"

data = {
    "client": "kkAUAzcqZu",
    "duration": "14",
    "fingerprint": "AQAAXEmVRFmiSEmE8EezZ8JLvMh7TBNf_LgH93gPP9gVntAVxnCHl8HNw89x5mgOlWKO8wi7XGjEMDgtIJ8udMKPH9Z04YeeC1Z5nMF3-MzxZrC6GC_EcEQ7esjRbJrRh0GOUT-6w1mMo-fRBz5RK4emB9t5PPCPc7huPFwCLaGyHEf-oeGyo2cK_DoiDc6O8zgeuOKhZ8djPAmyi3iWI_bxJ2ieQV3EIC81lNrRPMUzXMd3hJrK4qAOYoQgBgAKBGUCACAEIIAwIIAChhnglDNMGKQIQwoYwUBgAFgxiALGAMCUAEAIQpUBAgAAGFAUIEMRYMIIAZBBDAChRAI",
    # "fingerprint": "AQAAZGGSKEuUJEoU4coIHz_-F34CH5oWZTmO8DmakZmEl8eLvMc08cWPe3CP9_CDXeEJXWHg7niJP4ePp4IfaKKY4zzCLhcaMQxOC8inC53w44c1Hf_xXBBVHmfwwWcuvBmsLsYLMRzaMR1ylNOMxmGQY9TR_XAW4-h59IFP1Mqh6cF2Hg_84xyuG-8SaImkLMeRf2i47OhbHP8xzUiz4zyOB2LF49nxGE-C7MZzxM7xJ_AJTYuyIC81lFKO5kzxDD-eHaF2Fj-oAwSEAYAYIMAwQhADAAWCMgEAEEYAIwQFQAHDDHDKGSiMYIowBIRgoDlhxCAKGAMAUwIAIQhVBggKCAAMKAqYoQhQQYQAyABGAFBAKQQ",
#     # "trackid": "9662760c-93f8-41e5-a852-cbe1180ada65",
    "meta": "recording",
}

response = requests.post(url, params=data)

print("Status Code", response.status_code)
print("JSON Response ", response.json())
