from nose.tools import *
#import exp36_root #tutta la cartella
from exp36_root.potere import Personaggio


def test_potere():

    personaggio = Personaggio()
    assert_equal(personaggio.pom, False)
    personaggio.potere()
    assert_equal(personaggio.pom, True)
