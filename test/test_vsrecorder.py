import unittest


class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_add(self):
        pass

    def tearDown(self):
        print('test end')


if __name__ == '__main__':
    unittest.main()
