import json

def ans(ask):
    f = open('qna_kfm.json')
    data = json.load(f)
    return data[ask]