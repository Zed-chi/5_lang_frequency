import re
import sys
from collections import Counter


def load_data(filepath):
    if not filepath:
        raise OSError("empty path")
    with open(filepath, "r", encoding="utf-8") as text_file:
        return text_file.read()


def get_most_frequent_words(text, words_count):
    words = re.findall(r"[a-zA-Zа-яА-Я]+", text)
    words_with_frequency = Counter(words)
    if words_count is None or words_count > 0:
        return words_with_frequency.most_common(words_count)
    else:
        return []


def print_most_frequent_words(most_frequent_words):
    print("\nСлова:")
    for word, counter in most_frequent_words:
        print("{} - {}".format(word, counter))


def main():
    try:
        words_count = None
        if len(sys.argv) == 3:
            words_count = int(sys.argv[2])
        if len(sys.args) == 2:
            path_to_text = sys.argv[1]
        else:
            exit("Empty Path")
        text = load_data(path_to_text)
        most_frequent_words = get_most_frequent_words(text, words_count)
    except OSError as err:
        print("{}".format(err))
    except ValueError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words)


if __name__ == "__main__":
    main()
