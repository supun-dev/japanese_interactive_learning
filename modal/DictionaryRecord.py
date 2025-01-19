from flask import json


class DictionaryRecord:
    def __init__(self, kanji, furigana, english):
        self.kanji = kanji
        self.furigana = furigana
        self.english = english

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)

    def to_dict(self):
        return self.__dict__
