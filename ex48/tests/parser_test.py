from nose.tools import *
from lexicon_root import lexicon
from lexicon_root import parser


def test_peek():
    word_list = [("noun","bear"), ("verb", "eat")]
    word_p = parser.peek(word_list)
    assert_equal(word_p, "noun")

    word_list = []
    word_p1 = parser.peek(word_list)
    assert_equal(word_p1, None)


def test_match():
    word_list = [("noun","bear"), ("verb", "eat")]
    word_m = parser.match(word_list, "noun")
    assert_equal(word_m, ("noun", "bear"))

    word_m1 = parser.match(word_list, "subject")
    assert_equal(word_m1, None)

    word_m2 = parser.match(word_list, "verb")
    assert_equal(word_m2, None)


def test_skip():
    #funziona solo se sono i primi e unici tipi di parola
    word_list = [("stop", "the"), ("stop", "damn"), ("noun", "game")]
    parser.skip(word_list, "stop")
    word_types = [word[0] for word in word_list] #list comprehension
    verifica = "stop" in word_types #verifica di trovarlo
    assert_equal(verifica, False)


def test_analisi_verbo():
    #funziona solo sulla prima parola della lista, al max con uno stop prima
    word_list = [("stop", "the"), ("verb", "chew"),("noun", "alligator")]
    verificaV = parser.analizza_verbo(word_list)
    assert_equal(verificaV, ("verb", "chew"))


def test_analisi_oggetto():
    #idem come sopra
    word_list = [("stop", "the"), ("noun", "chips")]
    verificaS = parser.analizza_oggetto(word_list)
    assert_equal(verificaS, ("noun", "chips"))


def test_analisi_soggetto():
    #idem come sopra
    word_list = [("stop", "the"), ("noun", "chips")]
    verificaS = parser.analizza_oggetto(word_list)
    assert_equal(verificaS, ("noun", "chips"))


def test_analisi_frase():
    #li becca tutti?
    word_list = [("verb", "play"), ("stop", "the"), ("stop", "damn"), ("noun", "game")]
    verificaF = parser.analizza_frase(word_list)
    assert_equal(verificaF.object, "game")





######### finire analisi gramm
