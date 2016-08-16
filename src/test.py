import src.regexs as regexs
import re

fo = open("../resources/brightscript.txt", "r+")
strToParse = fo.read(11)
i = 0
tokens = []
regexMatches = True
while i < len(strToParse):
    if regexMatches:
        for regex in regexs.List:
            match = re.match(regex[0], strToParse[i:], re.IGNORECASE)
            if match :
                if regex[1] != None:
                    try:
                        tokens.append(match.group(1))
                    except IndexError:
                        tokens.append(match.group())
                try:
                    i += len(match.group(1))
                except IndexError:
                    i += len(match.group())
                regexMatches = True
                break
            else:
                regexMatches = False
    else:
        print("not match found")
        break

print(tokens)
