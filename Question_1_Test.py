import Question_1_Sol
import pytest

@pytest.mark.concat
def Test_Question1(res):
    assert res == "'Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'"