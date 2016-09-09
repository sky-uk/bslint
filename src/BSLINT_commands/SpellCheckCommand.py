import sys
import enchant
import os
import src.Constants as const
import src.ErrorMessagesBuilder.ErrorBuilder.ErrorMessagesConstants as ErrConst


class SpellCheckCommand(object):

    @staticmethod
    def execute(params):
        dictionary = params["dictionary"]
        personal_words_list = SpellCheckCommand.personal_words_filepath()
        d = enchant.DictWithPWL(dictionary, personal_words_list)
        if params['type'] == const.COMMENT:
            words = SpellCheckCommand._parse_comment_words(params['token'])
        else:
            words = SpellCheckCommand._parse_words(params['token'])

        for word in words:
            spelt_correct = d.check(word)
            if not spelt_correct:
                return {"error_key": ErrConst.TYPO_IN_CODE, "error_params": []}

    @staticmethod
    def _parse_words(identifier_str):
        words = []
        word = ''

        for i in range(0, len(identifier_str)):
            char = identifier_str[i]
            if not char.isalpha():
                if not word == '':
                    words.append(word)
                word = ''
                continue
            if char.islower():
                word += char
            elif char.isupper():
                if not word == '':
                    words.append(word)
                word = ''
                word += char
            elif char == '_' and word != '':
                words.append(word)
                word = ''
        if not word == '':
            words.append(word)

        return words

    @staticmethod
    def _parse_comment_words(comment):
        words = []
        comment_list = comment.split(' ')

        for word in comment_list:
            if not word.isalpha():
                continue
            if word == 'rem':
                continue
            if word.isupper():
                continue
            else:
                if not word == '':
                    words.append(word)
        return words

    @staticmethod
    def personal_words_filepath():
        if sys.argv[0].endswith('bslint'):

            this_dir, this_filename= os.path.split(__file__)
            personal_words_list = os.path.join(this_dir, "../config/personal-words-list.txt")

        elif sys.argv[0].endswith('nosetests'):
            personal_words_list = "./src/config/personal-words-list.txt"
        else:
            personal_words_list = "../src/config/personal-words-list.txt"

        return personal_words_list