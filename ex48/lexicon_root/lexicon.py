directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]

def tuple_maker(word):

    test_word = word.lower()

    if test_word in directions:
        return ('direction', word)
    elif test_word in verbs:
        return ('verb', word)
    elif test_word in stop_words:
        return ('stop', word)
    elif test_word in nouns:
        return ('noun', word)
    elif test_word.isdigit():
        return ('number', int(word))
    else:
        return ('error', word)

def scan(sentence):

    words = sentence.split()
    return [tuple_maker(word) for word in words]
