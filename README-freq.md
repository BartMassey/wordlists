# Frequently Used Word List
Copyright (c) 2019 Bart Massey

The files `freq.txt.gz` and `freq-words.txt.gz` provided
here are my attempt to provide a "frequently used word
list".

`freq.txt.gz` currently contains about 60,000 words and
their frequencies, separated on the line by a space
character; `freq-words.txt.gz` is the same words without the
frequencies.

## Rationale

This list represents my attempt to provide a "good"
dictionary for puzzles, etc. This list attempts to meet
several criteria:

* The list should contain only American spellings of
  American English words. (A British version of this list
  would be a good addition: patches welcome.)

* Proper names and foreign words should be excluded from the
  list.

* Words in this list should be "common", such that they
  might reasonably be found in writing intended for the
  general public.

## Provenance and Methodology

In an attempt to achieve the list's rationale, I have
proceeded as follows:

* Obtained a copy of `count_1w.txt`, YAWL, EOWL, SCOWL, and
  ENABLE 2K: see [`README.md`](README.md) for
  details on the word lists.

* Wrote a Python 3 program [`merge.py`](merge.py) to merge
  these lists as follows:

  * Exclude all capitalized, non-ASCII, and
    non-alphabetic-containing words from each list.
  
  * Exclude all one-letter words from each list.

  * Exclude all words that do not appear in the
    Google/Norvig list, the SCOWL list, and at least one of
    the YAWL, EOWL and ENABLE 2K lists.

  * Add back "a" and "i" (lowercase) to the result.

  * Save the resulting words and their counts, with word and
    count seperated by an ASCII space and UNIX line endings
    (ASCII LF).

A scan of the resulting list looks reasonably sane, and
seems to match the goals set forth in the rationale.

## License

This work is made available under the
[MIT License](https://opensource.org/licenses/mit-license.php). Please
see the link for license terms.
