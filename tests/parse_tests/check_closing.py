import unittest

from bslint import constants as const
from bslint.parser.parser import Parser


class TestCheckClosingTest(unittest.TestCase):

    def testEndIf(self):
        parser = Parser()
        result = parser.parse("endif")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_IF], parser.all_statements[0])

    def testEndIfSpace(self):
        parser = Parser()
        result = parser.parse("end if")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_IF], parser.all_statements[0])

    def testEndWhile(self):
        parser = Parser()
        result = parser.parse("endwhile")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_WHILE], parser.all_statements[0])

    def testEndWhileSpace(self):
        parser = Parser()
        result = parser.parse("end while")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_WHILE], parser.all_statements[0])

    def testEndFor(self):
        parser = Parser()
        result = parser.parse("endfor")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FOR], parser.all_statements[0])

    def testEndForSpace(self):
        parser = Parser()
        result = parser.parse("end for")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FOR], parser.all_statements[0])

    def testEndSub(self):
        parser = Parser()
        result = parser.parse("endsub")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_SUB], parser.all_statements[0])

    def testEndSubSpace(self):
        parser = Parser()
        result = parser.parse("end sub")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_SUB], parser.all_statements[0])

    def testEndFunction(self):
        parser = Parser()
        result = parser.parse("endfunction")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FUNCTION], parser.all_statements[0])

    def testEndFunctionSpace(self):
        parser = Parser()
        result = parser.parse("end function")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FUNCTION], parser.all_statements[0])

    def testEnd(self):
        parser = Parser()
        result = parser.parse("end")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END], parser.all_statements[0])
