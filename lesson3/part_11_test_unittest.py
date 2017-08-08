import unittest
from part_11 import  get_format_name

class NameTestCase(unittest.TestCase):
    '''Test for get_format_name function'''
    def test_get_format_name(self):
        format_name = get_format_name('joni', 'dep')
        self.assertEqual(format_name, 'Joni Dep')

    def test_get_format_middle_name(self):
        format_name = get_format_name('joni', 'dep', 'bruno')
        self.assertEqual(format_name, 'Joni Bruno Dep')

if __name__ == '__main__':
    unittest.main()