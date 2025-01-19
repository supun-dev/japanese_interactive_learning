from csv_file_handler.read_csv_file import search_japanese_word_by_english_meaning


def main():
    file_path = "resources\\vocabulary_N5.csv"
    search_japanese_word_by_english_meaning(file_path,"blue");

if __name__ == "__main__":
    main()