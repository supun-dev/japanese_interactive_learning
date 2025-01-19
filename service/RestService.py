from csv_file_handler.ReadCsvFile import search_japanese_word_by_english_meaning
from modal.DictionaryRecord import DictionaryRecord


def get_records_by_english_word(english_word):
    file_path = "resources\\vocabulary_N5.csv"
    records = search_japanese_word_by_english_meaning(file_path, english_word)
    return handle_response_for_english_word(records, english_word)


def handle_response_for_english_word(records, english_word):
    if not records:
        return handle_no_records(english_word)
    entries = []
    for record in records:
        entry = DictionaryRecord(record[0], record[1], record[2])
        entries.append(entry.to_dict())
    return entries


def handle_no_records(english_word):
    return {
        "error": "No records found",
        "english_word": english_word
    }
