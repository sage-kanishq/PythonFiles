import calc
import pytest
@pytest.mark.parametrize("test_input,test_output",
                        [
                            (10,100),
                            (5,25),
                            (3,9)
                        ]
)
def test_square(test_input,test_output):
    result = calc.square(test_input)
    assert result == test_output


