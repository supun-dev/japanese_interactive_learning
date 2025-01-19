import csv


def open_and_read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        # list() loads rows into memory. This is to prevent => ValueError: I/O operation on closed file.
        return list(csv.reader(csvfile, delimiter=',', quotechar='"'))


def print_csv_file(file_name):
    reader = open_and_read_csv(file_name)
    for row in reader:
        print(row)


def search_japanese_word_by_english_meaning(file_name, word):
    reader = open_and_read_csv(file_name)
    list_of_rows = []
    word_lower = word.lower()
    for row in reader:
        if any(word_lower in cell.lower() for cell in row):
            list_of_rows.append(row)
    if len(list_of_rows) != 0:
        return list_of_rows


def view_japanese_word_by_english_meaning(file_name, word):
    print("kanji : furigana : english")
    for row in search_japanese_word_by_english_meaning(file_name, word):
        print(" : ".join(row))
