import enchant
import os


def _get_new_dictionary(dictionary_lang="en_GB"):
    extra_words_filepath = _get_personal_words_filepath()
    return enchant.DictWithPWL(dictionary_lang, extra_words_filepath)


def _get_personal_words_filepath():
    this_dir, this_filename = os.path.split(__file__)
    file_path = os.path.join(this_dir, "../config/personal-words-list.txt")
    return file_path