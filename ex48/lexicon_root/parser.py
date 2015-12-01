#-*- coding: utf-8 -*-

class ParserError(Exception): #eccezione per dare errore
    pass

class Sentence(object):

    def __init__(self, subject, verb, obj):
        #per prendere tuple e convertirle
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    #dobbiamo decidere di quale tipo è la nostra frase, in base alla prossima parola
    #
    if word_list:
        word = word_list[0] #tupla
        return word[0] #primo pezzo della tupla: categoria lessicale
    else:
        return None


def match(word_list, expecting):
    #per consumare la parola -staccare la prima tupla- e andare avanti
    if word_list :
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip (word_list, word_type):
    #skip tutti i tipi di parole non utili
    while peek(word_list) == word_type:
        match(word_list, word_type)


#funzioni di analisi gramm.

def analizza_verbo(word_list):
    skip(word_list, "stop")

    if peek(word_list) == "verb":
        return match(word_list, "verb")
    else:
        raise ParserError("Mi aspetterei un verbo.")


def analizza_oggetto(word_list):
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        return match(word_list, "noun")
    elif next_word == "direction":
        return ("noun", "player")
    else:
        raise ParserError("Mi aspetterei un nome o una direzione.")


def analizza_soggetto(word_list):
    skip(word_list, "stop")
    next_word = peek(word_list)

    if next_word == "noun":
        return match(word_list, "noun")
    elif next_word == "verb":
        return ("noun", "player")
    else:
        raise ParserError("Mi aspetterei un verbo.")


#analisi dell'intera frase
def analizza_frase(word_list):
    subj = analizza_soggetto(word_list)
    verb = analizza_verbo(word_list)
    obj = analizza_oggetto(word_list)

    return Sentence(subj, verb, obj)
