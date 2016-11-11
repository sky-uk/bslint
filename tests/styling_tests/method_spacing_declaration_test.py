import os
import unittest
from filepaths import TEST_CONFIG_FILE_PATH
from filepaths import TESTS_CONFIG_PATH
from tests.resources.common.test_methods import CommonMethods as Common
import bslint


class TestMethodSpacingDeclaration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.active_method_spacing_declaration_config_path = os.path.join(
            TESTS_CONFIG_PATH, 'check_method_declaration/active_method_spacing_declaration.json')
        cls.common = Common()

    def test_valid_declaration(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("function declaration()", None)

    def test_indented_valid_declaration(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("  function declaration()", None)

    def test_valid_sub_declaration(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("sub declaration()", None)

    def test_valid_declaration_with_param(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("function declaration(a)", None)

    def test_valid_declaration_with_params(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("function declaration(a, b, c, d)", None)

    def test_invalid_declaration_with_no_space_between_params(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.common.method_dec_spacing("function declaration(a,b,c, d)", exp_result)

    def test_invalid_declaration_with_params(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.common.method_dec_spacing("function declaration(a, b, c,)", exp_result)

    def test_invalid_declaration_with_extra_spaces_in_params(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.common.method_dec_spacing("function declaration(a,   b, c,  d)", exp_result)

    def test_valid_declaration_with_extra_spaces_in_params(self):
        active_method_extra_spacing_declaration_config_path = os.path.join(
            TESTS_CONFIG_PATH, 'check_method_declaration/active_method_extra_spacing_declaration.json')
        bslint.load_config_file(user_filepath=active_method_extra_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        self.common.method_dec_spacing("function  declaration(a,  b)", None)

    def test_no_action_if_no_function_declared_on_line(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        exp_result = []
        self.common.lex_string("declaration(a  )", exp_result)

    def test_end_function_is_not_checked(self):
        bslint.load_config_file(user_filepath=self.active_method_spacing_declaration_config_path,
                                default_filepath=TEST_CONFIG_FILE_PATH)
        exp_result = []
        self.common.lex_string("end function", exp_result)
