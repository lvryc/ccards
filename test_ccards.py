# -*- encoding: utf-8 -*-

import ccards
from nose_parameterized import parameterized


@parameterized([
    (u"你好", [' '], ([], u"你好")),
    (u"说了很多比毛泽东还要狂热的话。",
     [' ', ' ', ' ', ' ', ' ', ' ', 'y', ' ', ' '],
     ([u'狂热'], u"说了很多比毛泽东还要狂热的话。")),
])
def test_answer(argument, monkey_ri, expected):
    test_ri = iter(monkey_ri)
    ccards.getch = lambda: next(test_ri)
    assert ccards.func(argument) == expected


@parameterized([
    (u'狂热', u'ku\xe1ng r\xe8'),
    (u'庐山会议', u'')
])
def test_get_pinyin(argument, expected):
    assert ccards.get_pinyin(argument) == expected


@parameterized([
    (u'狂热', u'极度热情。', u'狂热 - ku\xe1ng r\xe8 - 极度热情。')
])
def test_annotate(argument, definition, expected):
    ccards.raw_input = lambda _: definition
    assert ccards.annotate(argument) == expected


@parameterized([
    ([u'狂热'],
     [u'极度热情'],
     u"说了很多比毛泽东还要狂热的话。",
     u"""说了很多比毛泽东还要<b>狂热</b>的话。\t狂热 - ku\xe1ng r\xe8 - 极度热情\n"""),
])
def test_ankify(ukwords, definitions, passage, expected):
    mydefs = iter(definitions)
    ccards.raw_input = lambda _: next(mydefs)

    data = ccards.ankify(ukwords, passage)
    print data

    print expected
    assert data == expected
