import re

from .stopwords import remove_stopwords


def remove_punctuation(text: str):
    text = re.sub('[-]', ' ', text)
    return re.sub(u'[^a-zA-Z0-9áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]', '', text)


def clear_text(text: str) -> str:
    text = text.lower()
    text = remove_punctuation(text)
    text = remove_stopwords(text)
    return text


def clear_texts(texts: list) -> list:
    return list(map(lambda text: clear_text(text), texts))
