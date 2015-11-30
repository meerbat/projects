# -*- coding: utf-8 -*-
#Esercizio 36: nella foresta


class Personaggio(object):
    def __init__(self):
        self.pom = False

    def potere(self):
        self.pom = True

def start():
    personaggio = Personaggio()

start()
