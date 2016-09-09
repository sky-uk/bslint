import unittest
import src.ErrorMessagesBuilder.ErrorMessageHandler as ErrBuilder


class TestConfigFileLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.error = ErrBuilder.ErrorMessageHandler()

    def testReadJsonBadFileName(self):
        with self.assertRaises(ValueError):
            self.error.get("RANDOM_KEY")
