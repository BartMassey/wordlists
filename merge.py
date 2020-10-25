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
scowl = wordset("scowl-60.txt")
yawl = wordset("yawl-all.txt")
eowl = wordset("eowl.txt")
ws = scowl & (yawl | eowl)
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
result.sort(reverse=True)

with open("freq.txt", 'w') as f, open("freq-word.txt", 'w') as fw:
    for n, w in result:
        print(w, n, file=f)
        print(w, file=fw)
