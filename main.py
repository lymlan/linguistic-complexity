import requests
from pprint import pprint as print

from dictionary import get_word_definition

TEST_SENTENCE = "The nice boy takes an apple"

sentence = []




for word in TEST_SENTENCE.split(" "):
    possible_definitions = get_word_definition(word)
    sentence.append({'word': word, 'definitions': possible_definitions})


def is_determiner(word):
    for definition in word['definitions']:
        if definition.type == 'determiner':
            return True
    return False

def is_noun(word):
    for definition in word['definitions']:
        if definition.type == 'noun':
            return True
    return False

def is_type(word, type):
    for definition in word['definitions']:
        if definition.type == type:
            return True
    return False

def create_np_group(sentence, i):
    np_group = {"phrase_type" : "NP", "words": [sentence[i]['word']]}
    i += 1
    while True:
        if not i < len(sentence) or is_type(sentence[i], "verb"):
            break
        np_group['words'].append(sentence[i]['word'])
        i += 1
    print(i)
    return np_group, i

def group_subphrases(sentence):
    subphrases = []
    i = 0
    while i < len(sentence):
        item = sentence[i]
        print(item)
        if is_determiner(item):
            group, i = create_np_group(sentence, i)
            subphrases.append(group)
        elif is_type(item, 'verb'):
            subphrases.append({"phrase_type" : "VP", "words": [item['word']]})
            i += 1
        else:
            i += 1


    return subphrases


phrase_groups = group_subphrases(sentence)
print(group_subphrases(sentence))
type_translation = dict(VP="V", NP="X")
g = [type_translation[x["phrase_type"]] for x in phrase_groups]
print(F"The word order is {g}")


# print(sentence)
