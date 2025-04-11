from src.main import count_words_and_sentences
import pytest
import os


@pytest.fixture
def temp_text_file(request, text_content):
    def _create_file(text_content):
        file_path = 'D:\\Навчання\\CICD\\Middle test\\test_file.txt'
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text_content)

        # Фіксуємо закриття файлу після тесту
        def cleanup():
            if os.path.exists(file_path):
                os.remove(file_path)
        request.addfinalizer(cleanup)
        return file_path
    return _create_file


@pytest.mark.parametrize(
    "text_content, expected_word_count, expected_sentence_count",
    [
        ("Hello! This is a simple example.", 6, 2),
        ("Python is amazing, isn't it? Let's see how it works.", 10, 2),
        ("", 0, 0),
        ("One sentence only.", 3, 1),
        ("Wait... What?", 2, 2),
    ]
)
def test_count_words_and_sentences(temp_text_file,
                                   text_content,
                                   expected_word_count,
                                   expected_sentence_count):

    file_path = temp_text_file(text_content)

    word_count, sentence_count = count_words_and_sentences(file_path)

    assert word_count == expected_word_count
    assert sentence_count == expected_sentence_count
