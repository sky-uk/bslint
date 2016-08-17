import src


fo = open("../resources/brightscript.txt", "r+")
strToParse = fo.read(11)

result = src.lexer(strToParse)