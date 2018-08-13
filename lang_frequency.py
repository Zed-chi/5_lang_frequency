import re
import sys
from collections import Counter


def load_data(filepath):
    if filepath == "":
        raise OSError("empty path")
    with open(filepath, "r", encoding="utf-8") as text_file:
        return text_file.read()


def get_most_frequent_words(text, limit):
    words = re.findall(r"[a-zA-Zа-яА-Я]+", text)
    words_with_frequency = Counter(words)
    return words_with_frequency.most_common(limit) if limit > 0 else None


def print_most_frequent_words(most_frequent_words):
    print("\nСлова:")
    for word, counter in most_frequent_words:
        print("{} - {}".format(word, counter))


def main():
    try:
        if len(sys.argv) > 1:
            path_to_text = sys.argv[1]
        else:
            exit("Empty path")
        text = load_data(path_to_text)
        words_limit = int(input(">Limit of words to print:"))
        # вот тут value error
        most_frequent_words = get_most_frequent_words(text, words_limit)
    except OSError as err:
        print("{}".format(err))
    except ValueError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words)


if __name__ == "__main__":
    main()
