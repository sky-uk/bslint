import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TESTS_PATH = os.path.join(ROOT_DIR, 'tests')
TESTS_RESOURCES_PATH = os.path.join(TESTS_PATH, 'resources')
TESTS_CONFIG_PATH = os.path.join(TESTS_RESOURCES_PATH, 'config')
CONFIG_PATH = os.path.join(ROOT_DIR, 'bslint/config')

DEFAULT_CONFIG_FILE_PATH = os.path.join(CONFIG_PATH, 'default-config.json')
TEST_CONFIG_FILE_PATH = os.path.join(TESTS_CONFIG_PATH, 'test-config.json')
BSLINT_COMMAND_CONFIG_PATH = os.path.join(TESTS_CONFIG_PATH, 'bslint_commands')
COMMENTS_CONFIG_PATH = os.path.join(TESTS_CONFIG_PATH, 'comments')

LEXING_TEST_FILES_PATH = os.path.join(TESTS_RESOURCES_PATH, 'lexing_test_files')
STYLING_TEST_FILES_PATH = os.path.join(TESTS_RESOURCES_PATH, 'styling_test_files')
EMPTY_LINES_TEST_FILES_PATH = os.path.join(TESTS_RESOURCES_PATH, 'empty_lines_test_files')
TRACE_TEST_FILES_PATH = os.path.join(TESTS_RESOURCES_PATH, 'trace_test_files')