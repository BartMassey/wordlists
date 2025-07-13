# Word Lists

These word lists are useful for puzzle solvers and the like.

* `freq-words.txt.gz`, `freq.txt.gz`: *Frequently Used Word List*  
  This list of about 52,000 words is based on Peter Norvig's
  300,000 word ngram frequency list, which was built from
  Google's *Web Trillion Word Corpus*; this list was
  filtered to include only "reasonable" words. Each word is
  accompanied in `freq.txt.gz` by its frequency of use in
  the Google corpus; `freq-words.txt.gz` contains only the
  words. The file [`README.freq.md`](README.freq.md) in this
  distribution contains copyright and license as well as
  other information, including a detailed description of
  list construction.

* `eowl.txt.gz`: *The English Open Word List (EOWL)*  
  This list is compiled by Ken Loge based on the UK Advanced
  Cryptics Dictionary by J. Ross Beresford. It is reasonably
  comprehensive, with the significant limitation that it
  only includes words of 10 or fewer letters. The file
  [`README.eowl-official.html`](README.eow-official.html) in
  this distribution contains copyright and license as well
  as other information.

* `scowl.txt.gz`, `scowl-`*nn*`.txt.gz`: *Spell Checker Oriented Word List (SCOWL)*  
  Kevin Atkinson compiled this list from a variety of
  sources. The default list here is the "size 60 american"
  list.  The file
  [`README.scowl-official.txt`](README.scowl-official.txt)
  in this distribution contains copyright and license as
  well as other information. The files
  `README.scowl-`*nn*`.txt` contain source and settings
  information for the various dictionaries.

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

* `enable2k.txt.gz`: *ENABLE 2K Word List*  
  The Enhanced North American Benchmark LExicon (ENABLE)
  word list was constructed as a high-quality alternative to
  copyrighted official Scrabble dictionaries by Alan Beale
  and others: it is generally more permissive than EOWL,
  although it is not a superset.
  
  This "2K" edition is the latest available edition I am
  aware of, downloaded from the Internet Archive
  [here](https://web.archive.org/web/20090122025747/http://personal.riverusers.com/~thegrendel/enable2k.zip).
  This list was placed in the Public Domain by its creators.

  The file [`README-enable2k.txt`](README-enable2k.txt) in this
  distribution is taken from the official distribution of
  ENABLE 2K. It contains copyright and license as well as
  other information.

To use these lists, `gunzip` them. The result will have UNIX
line-endings (ASCII LF) which may need help on non-UNIX
boxes. The shell script `mkdict.sh` may be useful in
installing these on your machine.

The Scrabble&trade; SOWPODS/NASPA list and the Collins list
are not made available here due to copyright concerns.
