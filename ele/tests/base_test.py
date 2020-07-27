import pytest

from ele.element import elements

class BaseTest:
    @pytest.fixture
    def Sodium(self):
        return elements[10]

    @pytest.fixture
    def Magnesium(self):
        return elements[11]
