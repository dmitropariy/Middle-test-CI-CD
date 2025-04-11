import re


#функція підрахунку слів та речень
def count_words_and_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    words = re.findall(r'\b\w+(?:\'\w+)?\b', text)
    word_count = len(words)

    sentences = re.findall(r'[^.!?]+[.!?]+(?:\.\.\.)?', text)
    sentence_count = len(sentences)

    return word_count, sentence_count


#точка входу в програму
def main():
    path = input('Введіть шлях до файлу: ')
    word_count, sentence_count = count_words_and_sentences(path)
    print('Кількість слів:', word_count, 'Кількість речень:', sentence_count)

if __name__ == '__main__':
    main()