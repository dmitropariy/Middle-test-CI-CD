from src.main import count_words_and_sentences
import pytest
import os

@pytest.fixture
def temp_text_file(request, text_content):
    file_path = 'D:\Навчання\CICD\Middle test\\test_file.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text_content)
    def cleanup():
        if os.path.exists(file_path):
            os.remove(file_path)
    request.addfinalizer(cleanup)
    return file_path