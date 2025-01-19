from flask import Flask, json, jsonify

from service.RestService import get_records_by_english_word

api = Flask(__name__)


@api.route('/searchWordByEnglishMeaning/<english_word>', methods=['GET'])
def search_word_by_english_meaning(english_word):
    return jsonify(get_records_by_english_word(english_word))
