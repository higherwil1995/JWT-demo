import pytest
from main import round

def test_main():
    assert round(3.4, 0) == 3
    assert round(3.5, 0) == 4
    assert round(3.6, 0) == 4
