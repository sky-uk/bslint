import unittest

from bslint import constants as const
from bslint.parser.parser import Parser


class TestCheckClosingTest(unittest.TestCase):

    def test_end_if(self):
        parser = Parser()
        result = parser.parse("endif")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_IF], parser.all_statements[0])

    def test_end_if_space(self):
        parser = Parser()
        result = parser.parse("end if")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_IF], parser.all_statements[0])

    def test_end_while(self):
        parser = Parser()
        result = parser.parse("endwhile")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_WHILE], parser.all_statements[0])

    def test_end_while_space(self):
        parser = Parser()
        result = parser.parse("end while")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_WHILE], parser.all_statements[0])

    def test_end_for(self):
        parser = Parser()
        result = parser.parse("endfor")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FOR], parser.all_statements[0])

    def test_end_for_space(self):
        parser = Parser()
        result = parser.parse("end for")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FOR], parser.all_statements[0])

    def test_end_sub(self):
        parser = Parser()
        result = parser.parse("endsub")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_SUB], parser.all_statements[0])

    def test_end_sub_space(self):
        parser = Parser()
        result = parser.parse("end sub")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_SUB], parser.all_statements[0])

    def test_end_function(self):
        parser = Parser()
        result = parser.parse("endfunction")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FUNCTION], parser.all_statements[0])

    def test_end_function_space(self):
        parser = Parser()
        result = parser.parse("end function")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_FUNCTION], parser.all_statements[0])

    def test_end(self):
        parser = Parser()
        result = parser.parse("end")
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END], parser.all_statements[0])
