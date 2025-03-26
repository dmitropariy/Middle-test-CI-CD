import re

def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)

    sentences = re.findall(r'[^.!?]+[.!?]+(?:\.\.\.)?', text)
    sentence_count = len(sentences)

    return word_count, sentence_count