from .text import clear_texts


def generate_vocabulary(texts: list):
    texts = clear_texts(texts)
    words_list = generate_words_list(texts)


def generate_words_list(texts: list) -> list:
    words_list = []
    for text in texts:
        words_in_text = text.split()
        words_list += list(filter(lambda word: word not in words_list, words_in_text))
    return words_list


def generate_two_words_list(texts: list) -> list:
    two_words_list = []
    for text in texts:
        for two_words in merge_two_words(text):
            if two_words not in two_words_list:
                two_words_list.append(two_words)
    return two_words_list


def merge_two_words(text: str):
    words_in_text = text.split()
    for index, word in enumerate(words_in_text):
        if len(words_in_text) > index + 1:
            yield words_in_text[index] + ' ' + words_in_text[index + 1]

