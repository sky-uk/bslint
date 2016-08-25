import enchant


class SpellCheckCommand(object):

    @staticmethod
    def execute(params):
        d = enchant.Dict("en_UK")
        words = SpellCheckCommand._parse_words(params['token'])

        for word in words:
            spelt_correct = d.check(word)
            if not spelt_correct:
                return "Warning. You have spelling mistakes in your code. line number:x"

        return ""

    @staticmethod
    def _parse_words(identifier_str):
        words = []
        word = ''

        for i in range(0, len(identifier_str)):
            char = identifier_str[i]
            if not char.isalpha():
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
