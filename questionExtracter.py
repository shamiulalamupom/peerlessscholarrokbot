import requests
import json
# import cv2
import os

from dotenv import load_dotenv
load_dotenv()

def question_by_url(url, overlay=False, api_key=os.environ.get("API_KEY"), language='eng'):
    payload = {'url': url,
               'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    r = requests.post('https://api.ocr.space/parse/image',
                      data=payload,
                      )
    rd = r.content.decode()
    # res = json.dumps(rd, indent=2)
    res = json.loads(rd)
    res = res['ParsedResults'][0]['ParsedText']

    res = res.replace('Peerless Scholar - Preliminary', "")
    res = res.replace('\n', " ")
    res = res.replace('\r', '')
    res = res.replace('• ', '')

    if res.startswith('o'):
        res = res.replace('o', '', 1)

    fres = ''
    for ch in res:
        if ch == "?":
            break
        fres += ch

    fres += "?"

    return fres.replace(' ', '')