import os
import enchant

from filepaths import CONFIG_PATH


def get_new_dictionary(dictionary_lang="en_GB"):

    personal_words_list_path = os.path.join(CONFIG_PATH, 'personal-words-list.txt')
    return enchant.DictWithPWL(dictionary_lang, personal_words_list_path)
