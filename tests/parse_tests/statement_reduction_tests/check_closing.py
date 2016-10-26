import unittest

from bslint import constants as const
from bslint.parser.parser import Parser


class TestCheckClosingTest(unittest.TestCase):

    def _match(self, identifier):
        parser = Parser()
        result = parser.parse(identifier)
        self.assertEqual("Success", result['Status'])
        self.assertEqual([const.END_IF], parser.all_statements[0])

    def test_end_if(self):
        self._match("endif")

    def test_end_if_space(self):
        self._match("end if")

    def test_end_while(self):
        self._match("endwhile")

    def test_end_while_space(self):
        self._match("end while")

    def test_end_for(self):
        self._match("endfor")

    def test_end_for_space(self):
        self._match("end for")

    def test_end_sub(self):
        self._match("endsub")

    def test_end_sub_space(self):
        self._match("end sub")

    def test_end_function(self):
        self._match("endfunction")

    def test_end_function_space(self):
        self._match("end function")

    def test_end(self):
        self._match("end")
