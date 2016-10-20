import os
import enchant

from filepaths import CONFIG_PATH


def get_new_dictionary(dictionary_lang="en_GB"):

    PERSONAL_WORDS_LIST_PATH = os.path.join(CONFIG_PATH, 'personal-words-list.txt')
    return enchant.DictWithPWL(dictionary_lang, PERSONAL_WORDS_LIST_PATH)
