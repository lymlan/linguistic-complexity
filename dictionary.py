from dataclasses import dataclass
from typing import List

import requests

class TYPES:
    VERB = 1;
    NOUN = 2;


@dataclass
class Definition:
    word: str
    type: str



def get_word_definition(word) -> List[Definition]:
    response = requests.get(F'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')

    data = response.json()[0]['meanings']
    definitions = []
    for item in data:
        definitions.append(Definition(word=word, type=item['partOfSpeech']))

    return definitions
