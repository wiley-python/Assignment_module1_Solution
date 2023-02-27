import unittest
import q1


class MyTestCase(unittest.TestCase):
    def test_question1(self):
        str = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
        assert q1.question1() == str



if __name__ == '__main__':
    unittest.main()
