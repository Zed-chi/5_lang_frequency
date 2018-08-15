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


def get_arguments():
    parser = argparse.ArgumentParser(description='Word_frequency script')
    parser.add_argument('-p', required=True, dest="path_to_text")
    parser.add_argument('-c', default=10, dest="count_of_words", type=int)
    args = parser.parse_args()
    return args.count_of_words, args.path_to_text


def main():
    try:
        words_count, path_to_text = get_arguments()
        text = load_data(path_to_text)
        most_frequent_words = get_most_frequent_words(text, words_count)
    except OSError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words)


if __name__ == "__main__":
    main()
