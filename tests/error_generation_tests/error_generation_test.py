import unittest
import bslint.error_messages_builder.error_message_handler as err
import bslint.error_messages_builder.error_messages_constants as err_const


class TestErrorGeneration(unittest.TestCase):

    def testRandomKey(self):
        with self.assertRaises(ValueError) as ve:
            err.get_message("RANDOM_KEY")
        self.assertEqual(err_const.NO_SUCH_KEY, ve.exception.args[0])
