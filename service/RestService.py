from csv_file_handler.ReadCsvFile import search_japanese_word_by_english_meaning
from modal.DictionaryRecord import DictionaryRecord


def get_records_by_english_word(english_word):
    entries = []
    file_path = "resources\\vocabulary_N5.csv"
    records = search_japanese_word_by_english_meaning(file_path, english_word)
    for record in records:
        print(record)
    for record in records:
        entry = DictionaryRecord(record[0], record[1], record[2])
        entries.append(entry.to_dict())
    return entries
