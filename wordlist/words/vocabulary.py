from .text import clear_texts


def generate_vocabulary(texts: list, result_filter: list = []):
    texts = clear_texts(texts)
    words_list = generate_words_list(texts)
    two_words_list = generate_two_words_list(texts)

    vocabulary = {
        'textos': texts,
        'listaDePalavras': words_list,
        'listaDeDuasPalavras': two_words_list,
        'vetorDePalavras': generate_vectors(word_list=words_list, texts=texts),
        'vetorDeDuasPalavras': generate_vectors(word_list=two_words_list, texts=texts)
    }

    if not result_filter:
        return vocabulary

    filtered_vocabulary = {key: val for key, val in vocabulary.items() if key in result_filter}
    return filtered_vocabulary


def generate_words_list(texts: list) -> list:
    words_list = []
    for text in texts:
        words_in_text = text.split()
        for word in words_in_text:
            if word not in words_list:
                words_list.append(word)
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


def generate_vectors(word_list: list, texts: list) -> list:
    vectors = []
    for text in texts:
        vectors.append([text.count(word_list_item) for word_list_item in word_list])
    return vectors
