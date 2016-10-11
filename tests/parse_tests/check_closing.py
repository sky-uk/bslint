import unittest
from bslint import constants as const
from bslint.parser.parser import Parser


class TestCheckClosingTest(unittest.TestCase):

    def check_result(self, str_to_parse, expected):
        parser = Parser()
        parser.parse(str_to_parse)
        self.assertEqual(expected, parser.statement)

    def testEndIf(self):
        self.check_result('endif', [const.END_IF])

    def testEndIfSpace(self):
        self.check_result('end if', [const.END_IF])

    def testEndWhile(self):
        self.check_result('endwhile', [const.END_WHILE])

    def testEndWhileSpace(self):
        self.check_result('end while', [const.END_WHILE])

    def testEndFor(self):
        self.check_result('endfor', [const.END_FOR])

    def testEndForSpace(self):
        self.check_result('end for', [const.END_FOR])

    def testEndSpace(self):
        self.check_result('endsub', [const.END_SUB])

    def testEndSub(self):
        self.check_result('end sub', [const.END_SUB])

    def testEndFunction(self):
        self.check_result('endfunction', [const.END_FUNCTION])

    def testEndFunctionSpace(self):
        self.check_result('end function', [const.END_FUNCTION])

    def testEnd(self):
        self.check_result('end', [const.END])
