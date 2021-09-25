from pypinyin import lazy_pinyin
import json
import difflib
import os


def StringSimilar(str1: str, str2: str):
    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()

with open('names.json', 'r', encoding='utf-8') as fp:
    data = json.load(fp)

dirlist = os.listdir()

for i in data.items():
    uid = i[0]
    name = i[1][0]
    namepinyinl = lazy_pinyin(name, errors='default')
    namepinyin = ''
    for k in namepinyinl:
        namepinyin = namepinyin + k.lower()

    hsim = 0
    sub = ''
    for j in dirlist:
        sim = StringSimilar(namepinyin, j[:-4].lower())
        if sim > hsim:
            hsim = sim
            sub = j
    print(name, namepinyin, sub, hsim)
