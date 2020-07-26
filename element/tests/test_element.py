import pytest

from element import element_from_symbol
from element import element_from_name
from element import element_from_atomic_number
from element import element_from_mass

from element.tests.base_test import BaseTest

from element.exceptions import ElementError
from element.element import Sodium, Magnesium


class TestElement(BaseTest):
    def test_element_from_symbol(self):
        na = element_from_symbol("Na")
        assert na == Sodium
        na = element_from_symbol("na")
        assert na == Sodium
        na = element_from_symbol("NA")
        assert na == Sodium

    def test_invalid_element_from_symbol(self):
        with pytest.raises(ElementError):
            na = element_from_symbol("Na0")
        with pytest.raises(ElementError):
            na = element_from_symbol("sodium")
        with pytest.raises(TypeError):
            na = element_from_symbol(11)

    def test_element_from_name(self):
        na = element_from_name("sodium")
        assert na == Sodium
        na = element_from_name("Sodium")
        assert na == Sodium
        na = element_from_name("SODIUM")
        assert na == Sodium

    def test_invalid_element_from_name(self):
        with pytest.raises(ElementError):
            na = element_from_name("Na")
        with pytest.raises(ElementError):
            na = element_from_name("sodiu")
        with pytest.raises(TypeError):
            na = element_from_name(11)

    def test_element_from_atomic_number(self):
        na = element_from_atomic_number(11)
        assert na == Sodium

    def test_invalid_element_from_atomic_number(self):
        with pytest.raises(TypeError):
            na = element_from_atomic_number(11.0)
        with pytest.raises(TypeError):
            na = element_from_atomic_number("sodiu")
        with pytest.raises(ElementError):
            na = element_from_atomic_number(300)

    def test_element_from_mass(self):
        na = element_from_mass(22.98)
        assert na == Sodium
        with pytest.warns(UserWarning):
            mg = element_from_mass(24.0, exact=False)
        assert mg == Magnesium
        with pytest.warns(UserWarning):
            mg = element_from_mass(24, exact=False)
        assert mg == Magnesium

    def test_invalid_element_from_mass(self):
        with pytest.raises(ElementError):
            na = element_from_mass(22)
        with pytest.raises(TypeError):
            na = element_from_mass("11.0")
        with pytest.raises(TypeError):
            na = element_from_mass("sodium")

    def test_element_attributes(self):
        na = element_from_mass(22.98)
        assert na.mass == 22.9898
        assert na.atomic_number == 11
        assert na.name == "sodium"
        assert na.symbol == "Na"
