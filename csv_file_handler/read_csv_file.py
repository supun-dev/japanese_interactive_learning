import csv

def open_and_read_csv(file_name):
    print("Reading csv file with Japanese characters:")
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        #list() loads rows into memory. This is to prevent => ValueError: I/O operation on closed file.
        return list(csv.reader(csvfile, delimiter=',', quotechar='"'))


def print_csv_file(file_name):
    print("Reading csv file with Japanese characters:")
    reader = open_and_read_csv(file_name)
    for row in reader:
        print(row)

def search_japanese_word_by_english_meaning(file_name,word):
    print("Searching word by english characters:")
    reader = open_and_read_csv(file_name)
    for row in reader:
        if word in row:
            print(row)