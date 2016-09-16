import unittest
import bslint.ErrorMessagesBuilder.error_message_handler as ErrBuilder


class TestConfigFileLoading(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.error = ErrBuilder.error_message_handler()

    def testReadJsonBadFileName(self):
        with self.assertRaises(ValueError):
            self.error.get("RANDOM_KEY")
