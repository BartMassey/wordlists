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

freqs = sys.argv[1]
ws = wordset(sys.argv[2])
if len(sys.argv) > 2:
    for fname in sys.argv[3:]:
        ws &= wordset(fname)
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
