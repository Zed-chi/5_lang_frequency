import operator
import re
from collections import Counter


def load_data(filepath):
    if filepath == "":
        raise OSError("empty path")
    with open(filepath, "r", encoding="utf-8") as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words = re.sub(r"\W", " ", text).split(" ")
    words_with_frequency = Counter()
    for word in words:
        if word != "":
            words_with_frequency[word] += 1
    return words_with_frequency


def print_most_frequent_words(most_frequent_words, limit=10):
    if limit > 0:
        print("\nСлова:")
        for word_with_counter in most_frequent_words.most_common(limit):
            print("{} - {}".format(word_with_counter[0], word_with_counter[1]))


def main():
    try:
        path_to_text = input(">Type path to your text: some.txt:")
        text = load_data(path_to_text)
        most_frequent_words = get_most_frequent_words(text)
        words_limit_to_print = int(input(">Limit of words to print:"))
    except OSError as err:
        print("{}".format(err))
    except ValueError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words, words_limit_to_print)


if __name__ == '__main__':
    main()
