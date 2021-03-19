import pytest

from ele import element_from_symbol
from ele import element_from_name
from ele import element_from_atomic_number
from ele import element_from_mass
from ele import infer_element_from_string
from ele import Elements

from ele.tests.base_test import BaseTest

from ele.exceptions import ElementError
from ele.exceptions import MultiMatchError


class TestElement(BaseTest):
    def test_element_from_symbol(self, Sodium):
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

    def test_element_from_name(self, Sodium):
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

    def test_element_from_atomic_number(self, Sodium):
        na = element_from_atomic_number(11)
        assert na == Sodium

    def test_invalid_element_from_atomic_number(self):
        with pytest.raises(TypeError):
            na = element_from_atomic_number(11.0)
        with pytest.raises(TypeError):
            na = element_from_atomic_number("sodiu")
        with pytest.raises(ElementError):
            na = element_from_atomic_number(300)

    def test_element_from_mass(self, Sodium, Magnesium):
        na = element_from_mass(22.98)
        assert na == Sodium
        with pytest.warns(UserWarning):
            mg = element_from_mass(24.0, exact=False)
        assert mg == Magnesium
        with pytest.warns(UserWarning):
            mg = element_from_mass(24, exact=False)
        assert mg == Magnesium
        elements = element_from_mass(289.0, duplicates="none")
        assert elements == None
        elements = element_from_mass(289.0, duplicates="all")
        fl = element_from_symbol("Fl")
        uup = element_from_symbol("Uup")
        assert elements == (fl, uup)
        elements = element_from_mass(288.5, duplicates="all", exact=False)
        assert elements == (fl, uup)

    def test_invalid_element_from_mass(self):
        with pytest.raises(ElementError):
            na = element_from_mass(22)
        with pytest.raises(TypeError):
            na = element_from_mass("11.0")
        with pytest.raises(TypeError):
            na = element_from_mass("sodium")
        with pytest.raises(TypeError):
            na = element_from_mass(22.99, duplicates="tuple")
        with pytest.raises(MultiMatchError):
            fl = element_from_mass(289.0)

    def test_invalid_element_from_string(self):
        with pytest.raises(TypeError):
            infer_element_from_string(22)

    def test_unmatched_element_from_string(self):
        with pytest.raises(ElementError):
            infer_element_from_string("compound")

    def test_infer_element_from_string(self):
        f = infer_element_from_string("F")
        assert f == Elements.F

        c = infer_element_from_string("carbon")
        assert c == Elements.C

        cl = infer_element_from_string("Chlorine")
        assert cl == Elements.Cl

    def test_element_attributes(self):
        na = element_from_mass(22.98)
        assert na.mass == 22.99
        assert na.atomic_number == 11
        assert na.name == "sodium"
        assert na.symbol == "Na"
        assert na.radius_bondi == 2.27
        assert na.radius_alvarez == 2.50

    def test_missing_attribute(self):
        uuo = element_from_atomic_number(118)
        assert uuo.radius_bondi is None
        assert uuo.radius_alvarez is None

    def test_repr(self):
        na = element_from_mass(22.98)
        print(na)

    def test_elements_enum(self):
        for key, val in Elements.symbols_dict.items():
            assert getattr(Elements, key) == val

    def test_hash(self):
        test_set = set()
        for symbol in Elements.symbols_dict:
            test_set.add(Elements.symbols_dict[symbol])
