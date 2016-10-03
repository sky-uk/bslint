import os
import unittest

import bslint
import bslint.utilities.commands as commands


class TestMethodSpacingDeclaration(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/styling_test_files/")

    def testValidDeclaration(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration()")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidSubDeclaration(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("sub declaration()")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithParam(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration(a)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithParams(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration(a, b, c, d)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithNoSpaceBetweenParams(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json",
                                default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration(a,b,c, d)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithParams(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration(a, b, c,)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithExtraSpacesInParams(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function declaration(a,   b, c,  d)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithExtraSpacesInParams(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_extra_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function  declaration(a,  b)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testNoActionIfNoFunctionDeclaredOnLine(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("declaration(a  )")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testEndFunctionIsNotChecked(self):
        bslint.load_config_file(user_filepath="check_method_declaration/active_method_spacing_declaration.json", default_filepath='test-config.json')
        result = commands.check_method_declaration_spacing("function  declaration(a,  b)\n\nend function")
        exp_result = None
        self.assertEqual(exp_result, result)
