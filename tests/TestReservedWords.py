import unittest
import src

class TestReservedWords(unittest.TestCase):

    def testIF(self):
        identifier = "IF"
        exp_result = [('IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTHEN(self):
        identifier = "THEN"
        exp_result = [('THEN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testELSEIF(self):
        identifier = "ELSE IF"
        exp_result = [('ELSE IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testELSE(self):
        identifier = "ELSE"
        exp_result = [('ELSE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDIF(self):
        identifier = "END IF"
        exp_result = [('END IF', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFOR(self):
        identifier = "FOR"
        exp_result = [('FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testTO(self):
        identifier = "TO"
        exp_result = [('TO', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEND(self):
        identifier = "END"
        exp_result = [('END', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testSTEP(self):
        identifier = "STEP"
        exp_result = [('STEP', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXITFOR(self):
        identifier = "EXIT FOR"
        exp_result = [('EXIT FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testFOREACH(self):
        identifier = "FOR EACH"
        exp_result = [('FOR EACH', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testIN(self):
        identifier = "IN"
        exp_result = [('IN', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDFOR(self):
        identifier = "END FOR"
        exp_result = [('END FOR', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testWHILE(self):
        identifier = "WHILE"
        exp_result = [('WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testENDWHILE(self):
        identifier = "END WHILE"
        exp_result = [('END WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)

    def testEXITWHILE(self):
        identifier = "EXIT WHILE"
        exp_result = [('EXIT WHILE', 'STMT')]
        result = src.lexer(identifier)
        self.assertEquals(result, exp_result)