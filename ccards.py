# -*- encoding: utf-8 -*-

import jieba
import logging
import sys
from getch import getch
jieba.setLogLevel(logging.INFO)
from cjklib.dictionary import CEDICT
c = CEDICT()


def func(passage):
    """
    Given a passage, runs through all words
    in the passage and prompts for whether
    they're known or not.

    Return ([list of unknown words], "full \
    passage")
    """

    myPassage = jieba.cut(passage)
    myString = ""
    unknown_words = []
    print "Press 'space' for every word you recognise. \
 Hit any other key to mark a word you don't recognise.\n"
    for i in myPassage:
        print i.encode('utf-8'),
        if getch() != ' ':
            unknown_words.append(i)
        myString += i
    print "\n"
    return (unknown_words, myString)


def get_pinyin(word):
    try:
        mine = next(c.getForHeadword(word))
        return mine[2]
    except StopIteration:
        return ''


def annotate(word):
    definition = raw_input("Definition of %s\n" % word.encode('utf-8'))
    try:
        return "%s - %s - %s" % (word,
                                 get_pinyin(word),
                                 definition)
    except UnicodeDecodeError:
        return "%s - %s - %s" % (word,
                                 get_pinyin(word),
                                 definition.decode('utf-8'))


def ankify(unknown_words, myString):
    myCSV = u""
    cutString = list(jieba.cut(myString))
    for i in unknown_words:
        bolded = "".join(["<b>%s</b>" % x if x == i else x for x in cutString])
        to_append = u"%s\t%s\n" % (bolded, annotate(i))
        myCSV += to_append

    return myCSV


if __name__ == "__main__":
    try:
        ofile = sys.argv[1]
    except:
        ofile = ""

    passage = raw_input("Please enter a Chinese sentence.\n").decode('utf-8')
    ukwords, passage = func(passage)
    if ofile:
        handle = open(ofile, 'a')
        handle.write(ankify(ukwords, passage).encode('utf-8'))
        handle.close()
    else:
        print ankify(ukwords, passage)
