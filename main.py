import requests
from pprint import pprint as print



TEST_SENTENCE = "The boy kisses the cute girl"
TEST_SENTENCE = "The boy gives the girl a kiss and a hug the cute girl"

sentence = []


def get_word_definition(word):
    response = requests.get(F'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')

    data = response.json()[0]['meanings']
    return data


def save_possible_class(word, api_response):
    sentence.append({"word": word, 'classes': [c['partOfSpeech'] for c in api_response]})



for word in TEST_SENTENCE.split(" "):
    response = get_word_definition(word)
    save_possible_class(word, response)

for word in sentence:
    if 'verb' in word['classes']:
        print(F"{word} can be a verb")



# print(sentence)
