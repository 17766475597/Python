import unittest
from name_function import get_fomatted_name

class NamesTestCase(unittest.TestCase):
    """测试name_function_py"""

    def test_first_last_name(self):
        """测试能够正确处理Jack Jones这种名字吗"""
        formmated_name = get_fomatted_name("jack","jones");
        self.assertEqual(formmated_name, 'Jack Jones')

unittest.main()