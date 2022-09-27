import pytest
from ..myFirstFlask.calculator import calculate_sum


def test_calculate_sum():
    assert calculate_sum(5, 3) == 8
    assert calculate_sum(1.5, 3.5) == pytest.approx(5.0)
