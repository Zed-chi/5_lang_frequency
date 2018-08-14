import re
import argparse
from collections import Counter


def load_data(filepath):
    if not filepath:
        raise OSError("empty path")
    with open(filepath, "r", encoding="utf-8") as text_file:
        return text_file.read()


def get_most_frequent_words(text, words_count):
    words = re.findall(r"[a-zа-я]+", text.lower())
    words_with_frequency = Counter(words)
    return words_with_frequency.most_common(words_count)


def print_most_frequent_words(most_frequent_words):
    print("\nWords:")
    for word, count in most_frequent_words:
        print("{} - {}".format(word, count))


def main():
    parser = argparse.ArgumentParser(description='Word_frequency script')
    parser.add_argument('-p', action="store", dest="path_to_text")
    parser.add_argument('-c', action="store", dest="count_of_words", type=int)
    args = parser.parse_args()
    try:
        words_count = args.count_of_words
        path_to_text = args.path_to_text
        if path_to_text is None:
            exit("Empty Path")
        text = load_data(path_to_text)
        most_frequent_words = get_most_frequent_words(text, words_count)
    except OSError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words)


if __name__ == "__main__":
    main()
