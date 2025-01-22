import csv


class ReadCsvFile:
    _list_of_rows = []

    @staticmethod
    def open_and_read_csv(file_name):
        if not ReadCsvFile._list_of_rows:
            with open(file_name, newline='', encoding='utf-8') as csvfile:
                # list() loads rows into memory. This is to prevent => ValueError: I/O operation on closed file.
                ReadCsvFile._list_of_rows = list(csv.reader(csvfile, delimiter=',', quotechar='"'))
        return ReadCsvFile._list_of_rows

    @staticmethod
    def print_csv_file(file_name):
        reader = ReadCsvFile.open_and_read_csv(file_name)
        for row in reader:
            print(row)

    @staticmethod
    def search_japanese_word_by_english_meaning(file_name, word):
        reader = ReadCsvFile.open_and_read_csv(file_name)
        list_of_rows = []
        word_lower = word.lower()
        for row in reader:
            if any(word_lower in cell.lower() for cell in row):
                list_of_rows.append(row)
        if len(list_of_rows) != 0:
            return list_of_rows

    @staticmethod
    def view_japanese_word_by_english_meaning(file_name, word):
        print("kanji : furigana : english")
        for row in ReadCsvFile.search_japanese_word_by_english_meaning(file_name, word):
            print(" : ".join(row))
