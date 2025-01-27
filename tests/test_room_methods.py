import unittest


import unittest

class TestRoomMethods(unittest.TestCase):

    def setUp(self):
        pass

    
    # Returns true if the string splits and matches
    # the given output.
    def test_get_item(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
