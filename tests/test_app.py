import pytest
from myapp.app import multiply_by_two, divide_by_two, calculate_area  # Added calculate_area

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]

class TestApp:
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

# Test for failure 
# this test will fail
def test_area():
    num = 65 # Last two digits of my student ID
    expected_area = 4225 # 65 * 65 = 4225
    calculate_area = num * num
    assert calculate_area == expected_area, f"Expected {expected_area}, but got {calculate_area}" 
