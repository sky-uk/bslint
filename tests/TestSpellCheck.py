import unittest
import src
import Constants as const


class TestSpellCheck(unittest.TestCase):
    def setUp(self):
        self.spellCheck = src.SpellCheckCommand()

    def testSingleLCase(self):
        test_string = "bad"
        exp_result = ''
        result = self.spellCheck.execute({'token' : test_string})
        self.assertEquals(result , exp_result)

    def testCamelCase(self):
        test_string = "badGood"
        exp_result = ''
        result = self.spellCheck.execute({'token' : test_string})
        self.assertEquals(result , exp_result)

    def testSingleUpperCase(self):
        test_string = "GOOD"
        exp_result = ''
        result = self.spellCheck.execute({'token' : test_string})
        self.assertEquals(result , exp_result)

    def testSingleUnderscore(self):
        test_string = "bad_Good"
        exp_result = ''
        result = self.spellCheck.execute({'token' : test_string})
        self.assertEquals(result , exp_result)