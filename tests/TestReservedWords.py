import unittest
import src


class TestReservedWords(unittest.TestCase):

    def setUp(self):
        self.lexer = src.Lexer()
        
    def testIF(self):
        identifier = "IF"
        exp_result = [('IF', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTHEN(self):
        identifier = "THEN"
        exp_result = [('THEN', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testELSE_IF(self):
        identifier = "ELSE IF"
        exp_result = [('ELSE IF', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testELSE(self):
        identifier = "ELSE"
        exp_result = [('ELSE', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_IF(self):
        identifier = "END IF"
        exp_result = [('END IF', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFOR(self):
        identifier = "FOR"
        exp_result = [('FOR', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testTO(self):
        identifier = "TO"
        exp_result = [('TO', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND(self):
        identifier = "END"
        exp_result = [('END', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testSTEP(self):
        identifier = "STEP"
        exp_result = [('STEP', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_FOR(self):
        identifier = "EXIT FOR"
        exp_result = [('EXIT FOR', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testFOR_EACH(self):
        identifier = "FOR EACH"
        exp_result = [('FOR EACH', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testIN(self):
        identifier = "IN"
        exp_result = [('IN', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_FOR(self):
        identifier = "END FOR"
        exp_result = [('END FOR', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testWHILE(self):
        identifier = "WHILE"
        exp_result = [('WHILE', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEND_WHILE(self):
        identifier = "END WHILE"
        exp_result = [('END WHILE', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)

    def testEXIT_WHILE(self):
        identifier = "EXIT WHILE"
        exp_result = [('EXIT WHILE', 'STMT')]
        result = self.lexer.lex(identifier)
        self.assertEquals(result, exp_result)