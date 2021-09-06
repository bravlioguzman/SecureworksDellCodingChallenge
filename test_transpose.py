import pytest
import os 
from os import path
from string import printable
from pathlib import Path

#Test file has data
def test_file_has_words():
	assert os.path.getsize("Words.txt") > 0

#Test that files has the correct name, looking for Words.txt for these TCs
def test_file_has_correct_name():
    assert os.path.exists("NotTheCorrectFileName.txt") == 0

#Test that file exists and has the correct name
def test_file_exits():
    assert os.path.exists("Words.txt") == 1

#Test that method returns a value
def test_returns_longest_word_transposed():
    from Transpose import longest_word_and_transpose
    str = print(longest_word_and_transpose('Words.txt'))
    assert str != ""

#Test file is no bigger than 1 GB
def test_file_no_bigger_than_one_gb():
    size = os.path.getsize("Words.txt")
    sizeInKb = size / 1024
    sizeInMb = sizeInKb / 1024
    assert not sizeInMb > 1000

#Test file has .txt extension
def test_file_has_txt_extension():
    assert Path("Words.txt").suffix == '.txt'

#Test file is accessible
def test_file_is_accessible():
    assert os.access("Words.txt", os.R_OK)

#Test alphanumeric or special chars
def test_alphanumeric_or_special_chars():
    from Transpose import longest_word_and_transpose
    text = longest_word_and_transpose("Words.txt")
    if set(text).difference(printable):
        print("Text file has special characters.")
        assert not text.isalnum()
    else:
        print("Text file does not have special characters.")
        assert text.isalnum()
