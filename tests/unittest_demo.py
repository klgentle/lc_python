import unittest


class TestDict(unittest.TestCase):

    def setUp(self):
        print('setUp...')

    def test_some_case(self):
        pass

    def tearDown(self):
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()
