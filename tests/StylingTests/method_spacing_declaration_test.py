import unittest
import bslint
import bslint.commands as commands
import bslint.ErrorMessagesBuilder.error_message_handler as Err
import bslint.ErrorMessagesBuilder.ErrorBuilder.error_messages_constants as ErrConst
import os


class TestMethodSpacingDeclaration(unittest.TestCase):
    WARNINGS = 'Warnings'
    STATUS = 'Status'
    SUCCESS = 'Success'

    @classmethod
    def setUpClass(cls):
        cls.error = Err.error_message_handler()
        this_dir, this_filename = os.path.split(__file__)
        cls.filepath_prefix = os.path.join(this_dir, "../resources/StylingTestFiles/")

    def testValidDeclaration(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration()")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidSubDeclaration(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("sub declaration()")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithParam(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration(a)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithParams(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration(a, b, c, d)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithNoSpaceBetweenParams(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json",
                                         default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration(a,b,c, d)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithParams(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration(a, b, c,)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testInvalidDeclarationWithExtraSpacesInParams(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function declaration(a,   b, c,  d)")
        exp_result = {'error_key': 'METHOD_DECLARATION_SPACING', 'error_params': []}
        self.assertEqual(exp_result, result)

    def testValidDeclarationWithExtraSpacesInParams(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_extra_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("function  declaration(a,  b)")
        exp_result = None
        self.assertEqual(exp_result, result)

    def testNoActionIfNoFunctionDeclaredOnLine(self):
        config = bslint.load_config_file(user="CheckMethodDeclaration/active_method_spacing_declaration.json", default='test-config.json')
        commands.config = config
        result = commands.check_method_declaration_spacing("declaration(a  )")
        exp_result = None
        self.assertEqual(exp_result, result)
