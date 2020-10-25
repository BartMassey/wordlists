# Word Lists

These word lists are useful for puzzle solvers and the like.

* `freq-words.txt.gz`, `freq.txt.gz`: *Frequently Used Word List*  
  This list of about 52,000 words is based on Peter
  Norvig's 300,000 word ngram frequency list, which was
  built from Google's *Web Trillion Word Corpus*; this list
  was filtered to include only dictionary words. Each word
  is accompanied in `freq.txt.gz` by its frequency of use in
  the Google corpus; `freq-words.txt.gz` contains only the
  words. The file [`README.freq.md`](README.freq.md) in this
  distribution contains copyright and license as well as
  other information, including a detailed description of
  list construction.

* `eowl.txt.gz`: *The English Open Word List (EOWL)*  
  This list is compiled by Ken Loge based on the UK Advanced
  Cryptics Dictionary by J. Ross Beresford. It is reasonably
  comprehensive. The file
  [`README.eowl-official.html`](README.eow-official.html) in this
  distribution contains copyright and license as well as
  other information.

* `scowl.txt.gz`: *Spell Checker Oriented Word List (SCOWL)*  
  Kevin Atkinson compiled this list from a variety of
  sources. The list here is the "size 40 american" list.
  The file [`README.scowl-official.txt`](README.scowl-official.txt) in this
  distribution contains copyright and license as well as
  other information.

* `yawl.txt.gz`, `yawl-sig.txt.gz`, `yawl-all.txt.gz`: *Yet Another Word List*  
  From Aaron Bull Schaefer's GitHub
  [archive](https://github.com/elasticdog/yawl) of Mendel
  Leo Cooper's word list built with the assistance of Alan
  Beale. `yawl-sig.txt` is a small list of optional words
  that might be added to `yawl.txt`: `yawl-all.txt.gz` is
  the sorted concatenation of these lists.  The files
  [`README.yawl-official.md`](README.yawl-official.md) and
  [`README.yawl-original.md`](README.yawl-original.md) in
  this distribution contain copyright and license as well as
  other information.

To use these lists, `gunzip` them. The result will have UNIX
line-endings (ASCII LF) which may need help on non-UNIX
boxes.

The official Scrabble&trade; SOWPODS list is not made
available here due to copyright concerns.
