# -*- coding: utf-8 -*-
#Esercizio 36: nella foresta
from sys import exit

pom = False
end = "\nE vissero tutti felici e contenti."
interr = "°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n"

class Personaggio(object):
    def __init__(self):
        self.pom = False

    def potere(self):
        self.pom = True

def drink_water(personaggio):
    print interr, "Ora hai un potere magico: \n il potere di saltare altissimo!"
    personaggio.potere()
    print "Utile, no?"
    print "Allora decidi: vuoi andare in montagna o restare qui?"
    choice_drink = raw_input("> ")
    if choice_drink == "montagna":
        mountains(personaggio)
    elif choice_drink == "qui":
        print interr, "Bevi altra acqua e puoi saltare sempre più alto, \nfinché finisci sulla Luna senza poter più tornare giù. Bravo!"
        print end
        exit(0)
    else:
        print interr, "Sei entusiasta del tuo nuovo potere, e continui a saltellare finché finisci le energie."



def dip_feet():
    print interr, "Ti togli quei calzini puzzolenti e finalmente pucci i piedini nell'acqua, ma una piovra te li afferra e ti porta giù con lei negli abissi."
    print end
    exit(0)

def singing_stream(personaggio):
    print interr, "Sei arrivato al fiume che canta: che fai?"
    print "Pucci i piedini stanchi o bevi quest'acqua scura?"
    choice_stream = raw_input("> ")

    if choice_stream == "puccio":
        dip_feet()
    elif choice_stream == "bevo":
        drink_water(personaggio)
    else:
        print interr, "Non scegliere è da ignavi: castigo eterno nell'antinferno immediato per te.", end
        exit(0)


def gold_found():
    print interr, "Orooo"
    print "Trova un modo per uscire da qui e scappa!"
    exit(0)

def cave_enter(personaggio):
    print interr, "Entri in una stanza stretta e buia, potrebbero esserci troll morti che ti guardano dalle loro orbite vuote, ma tu non lo sai."
    print "Vedi una piccola luce arrivare dall'alto."
    if personaggio.pom :
        print interr, "Spicchi un salto e arrivi verso la luce: è l'oro che luccica sul soppalco!"
        gold_found()
    else:
        print interr, "I troll si rianimano e ti mangiano pezzo per pezzo...gustoso!"
        exit(0)

def door_spit(personaggio):
    print interr, "La porta si offende e ti sputa, vuoi andare al fiume a lavarti?"
    choice_door = raw_input("> ")
    if choice_door == "sì":
        singing_stream(personaggio)
    elif choice_door == "no":
        print interr, "Che schifo! Torni a casa pieno di vergogna e muco di porta.", end
        exit(0)
    else:
        print interr, "Che noia, torni a casa.", end
        exit(0)



def mountains(personaggio):
    print interr, "Arrivi davanti ad una strana porta: \nche fai, entri o non entri?"
    print personaggio.pom
    choice_mount = raw_input("> ")

    if (choice_mount == "no" and personaggio.pom):
        print interr,"Bravo, c'è sangue di Troll su questa porta."
        print "Salti sopra la montagna e ci ricadi dentro da una botola: hai trovato l'oro!"
        gold_found()
    elif (choice_mount == "no" and not personaggio.pom):
        door_spit(personaggio)
    elif (choice_mount == "sì" or choice_mount == "entro"):
        cave_enter(personaggio)
    elif choice_mount == "si":
        print interr, "Non scrivi sì con l'accento, meriti le pene dell'inferno nel IX cerchio riservate ai traditori della patria.", end
        exit(0)
    else:
        door_spit(personaggio)



def start():
    personaggio = Personaggio()
    print "È una bella giornata di sole, e vai a fare una passeggiata tra le colline."
    print "Dopo un po' una montagna scura si staglia alla tua sinistra,\n e senti il canto di un ruscello alla tua destra."
    print "Dove vai?"
    choice_start = raw_input("> ")
    #print "BOH"
    if choice_start == "ruscello" or choice_start == "dx":
        #print "BEH"
        singing_stream(personaggio)
    elif choice_start == "montagna" or choice_start == "sx":
        #print "BAH"
        mountains(personaggio)
    else:
        #print "BUH"
        print interr, "Davvero? Si apre una voragine e t'inghiotte: ti porta direttamente al V cerchio, quello degli accidiosi."
        print "Divertiti immerso nello Stige.", end
        exit(0)

start()
