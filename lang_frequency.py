import operator
import re


def load_data(filepath):
    if filepath == "":
        raise OSError("Пустой путь")
    with open(filepath, "r", encoding="utf-8") as text_file:
        return text_file.read()


def get_most_frequent_words(text):
    words = re.sub(r"\W", " ", text).split(" ")
    words_with_frequency = dict()
    for word in words:
        if word != "" and word in words_with_frequency:
            words_with_frequency[word] += 1
        elif word != "":
            words_with_frequency[word] = 1
    sorted_words_list = sorted(
        words_with_frequency.items(),
        key=operator.itemgetter(1),
        reverse=True,
        )
    return sorted_words_list


def print_most_frequent_words(most_frequent_words, limit=10):
    if limit > 0:
        print("\nСлова:")
        for id in range(limit):
            word = most_frequent_words[id][0]
            count = most_frequent_words[id][1]
            print("{} - {}".format(word, count))


def main():
    try:
        path_to_text = input(">Введите путь к текстовому файлу:")
        text = load_data(path_to_text)
        most_frequent_words = get_most_frequent_words(text)
        words_limit_to_print = int(input(">Сколько слов вывести максимум?:"))
    except OSError as err:
        print("{}".format(err))
    except ValueError as err:
        print("{}".format(err))
    else:
        print_most_frequent_words(most_frequent_words, words_limit_to_print)


if __name__ == '__main__':
    main()
