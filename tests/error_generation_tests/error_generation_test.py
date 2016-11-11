import unittest
from bslint.messages import handler as msg_handler
import bslint.messages.error_constants as err_const


class TestErrorGeneration(unittest.TestCase):

    def test_random_key(self):
        with self.assertRaises(ValueError) as ve:
            msg_handler.get_error_msg("RANDOM_KEY")
        self.assertEqual(err_const.NO_SUCH_KEY, ve.exception.args[0])
