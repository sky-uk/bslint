import unittest
import bslint.error_messages_builder.error_message_handler as err


class TestConfigFileLoading(unittest.TestCase):

    def testReadJsonBadFileName(self):
        with self.assertRaises(ValueError):
            err.get_message("RANDOM_KEY")
