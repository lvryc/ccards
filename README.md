ccards
======

Chinese Cards -- a small script for breaking a difficult phrase into Anki flashcards

Instructions for use
====================

* Run python ccards.py [output-file (optional)]
* At the prompt, type in a Chinese sentence.
* For every word that jieba identifies, press either 'space' if you recognise it or any other character if you don’t.
* Fill in definitions as appropriate.
* Import generated cards into Anki!

Requirements
============

1. Requires Jieba, cjklib, ltchinese (nose and nose-parameterized to run tests)
2. You may also need to install CEDICT, which can be done with `sudo installcjkdict CEDICT`.
