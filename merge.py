#!/usr/bin/python3

import sys

def wordset(fname):
    ws = set()
    with open(fname, 'r') as f:
        for w in f:
            ww = w.strip()
            if len(ww) < 2:
                continue
            if not (ww.isascii() and ww.islower() and ww.isalpha()):
                continue
            ws.add(ww)
    return ws

freqs = "count_1w.txt"
scowl = wordset("scowl.txt")
yawl = wordset("yawl-all.txt")
eowl = wordset("eowl.txt")
enable2k = wordset("enable2k.txt")
ws = scowl & (yawl | eowl | enable2k)
ws.add("a")
ws.add("i")
    
result = list()
with open(freqs, 'r') as f:
    for wl in f:
        w, n = wl.split()
        if w not in ws:
            continue
        n = int(n)
        result.append((n, w))

result.sort(key=lambda r: r[0], reverse=True)
with open("freq.txt", 'w') as f:
    for n, w in result:
        print(w, n, file=f)

result.sort(key=lambda r: r[1])
with open("freq-word.txt", 'w') as fw:
    for _, w in result:
        print(w, file=fw)
