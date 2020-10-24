from typing import List

from wordvector.words.stopwords import remove_stopwords_from_list


def generate_vocabulary(texts: List[str]):
    texts = remove_stopwords_from_list(texts)
    print(texts)
