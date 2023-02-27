import q1
import q2
import q3


def test_question1():
    str = ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
    assert q1.question1() == str


def test_question2():
    exp = '2510'
    assert q2.question2(q2.str1) == exp


def test_question3():
    str1 = '##Jon is #developer # musician##'
    assert q3.question3(q3.str1) == str1


