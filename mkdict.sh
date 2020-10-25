#!/bin/sh
DICT=/usr/local/share/dict
mkdir -p $DICT
for d in freq.txt yawl.txt eowl.txt
do
    gunzip <$d.gz >$DICT/$d
done
gunzip <freq-word.txt.gz >$DICT/freq.txt
gunzip <scowl-80.txt.gz >$DICT/scowl.txt
gunzip <yawl.txt.gz >$DICT/yawl.txt
gunzip <eowl.txt.gz >$DICT/eowl.txt
cat >$DICT/README-wordlists.txt <<'EOF'
The dictionaries freq.txt, yawl.txt, eowl.txt and scowl.txt
are from the wordlists project:
http://github.com/BartMassey/wordlists.  Please see that
repository for details.
EOF
