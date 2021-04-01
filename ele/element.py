import json
import warnings

from collections import namedtuple
from pathlib import Path

from ele.exceptions import ElementError
from ele.exceptions import MultiMatchError

JSON_PATH = Path.joinpath(Path(__file__).parent, "lib/elements.json")

__all__ = (
    "element_from_name",
    "element_from_mass",
    "element_from_atomic_number",
    "element_from_symbol",
    "Elements",
)


class Element(namedtuple("Element", "atomic_number, name, symbol, mass, radius_bondi, radius_alvarez")):
    """Chemical element object

    Template to create a chemical element.
    Properties of the element instance are immutable.
    All known elements are pre-built and stored internally.

    Parameters
    ---------
    name : str
        Name of the element.
    symbol : str
        Chemical symbol of the element.
    atom_number : int
        Atomic number of the element.
    mass : float
        Mass of the element in amu

    Return
    ------
    Element instance
        An immutable instance of this class.
    """

    def __repr__(self):
        return "Element: {}, symbol: {}, atomic number: {}, mass: {}".format(
            self.name, self.symbol, self.atomic_number, self.mass
        )

    def __hash__(self):
        return hash((self.name, self.symbol, self.atomic_number, self.mass))

    def __eq__(self, other):
        return hash(self) == hash(other)


def element_from_symbol(symbol):
    """Search for an element by its symbol

    Look up an element from a list of known elements by symbol.

    Parameters
    ----------
    symbol : str
        Element symbol

    Returns
    -------
    matched_element : element.Element
        The matching element from the periodic table

    Raises
    ------
    ElementError
        If no match is found
    """
    if not isinstance(symbol, str):
        raise TypeError(
            f"`string` ({symbol}) must be a string.  Provided {type(symbol).__name__}."
        )

    symbol = symbol.capitalize()
    matched_element = symbol_dict.get(symbol)
    if matched_element is None:
        raise ElementError(f"No element with symbol {symbol}")

    return matched_element


def element_from_name(name):
    """Search for an element by its name

    Look up an element from a list of known elements by name.

    Parameters
    ----------
    name : str
        Element name to look for, digits and spaces are removed before search

    Returns
    -------
    matched_element : element.Element
        The matching element from the periodic table

    Raises
    ------
    ElementError
        If no match is found
    """
    if not isinstance(name, str):
        raise TypeError(
            f"`string` ({name}) must be a string.  Provided {type(name).__name__}."
        )

    name = name.lower()
    matched_element = name_dict.get(name)
    if matched_element is None:
        raise ElementError(f"No element with name {name}")

    return matched_element


def element_from_atomic_number(atomic_number):
    """Search for an element by its atomic number

    Look up an element from a list of known elements by atomic number.

    Parameters
    ----------
    atomic_number : int
        Element atomic number

    Returns
    -------
    matched_element : element.Element
        The matching element from the periodic table

    Raises
    ------
    ElementError
        If no match is found
    """
    if not isinstance(atomic_number, int):
        raise TypeError(
            f"`string` ({atomic_number}) must be an integer.  Provided {type(atomic_number).__name__}."
        )

    matched_element = atomic_dict.get(atomic_number)
    if matched_element is None:
        raise ElementError(f"No element with atomic number {atomic_number}")

    return matched_element


def element_from_mass(mass, exact=True, duplicates="error"):
    """Search for an element by its mass

    Look up an element from a list of known elements by mass (amu).
    By default, requires that the element mass match exactly
    to the first digit after the decimal. Using `exact=False`
    will switch this behavior to return the element with the
    closest mass.

    Parameters
    ----------
    mass : int, float
        Element mass in amu
    exact : bool, optional,  default=True
        Require that the mass match to the first decimal. If False, the
        element with the closest mass will be returned
    duplicates : enum, optional, default="error"
        How to handle duplicate elements with the same mass.
        Error ("error"), return a tuple ("all"), or return
        None ("none")

    Returns
    -------
    matched_element : element.Element or tuple of element.Element
        The matching element(s) from the periodic table
    """
    if not isinstance(mass, (int, float)):
        raise TypeError(
            f"`string` ({mass}) must be a number.  Provided {type(mass).__name__}."
        )

    if duplicates.lower() not in ["error", "all", "none"]:
        raise TypeError(
            "`duplicates` must be one of the following: `error`, `all`, `none`"
        )
    mass = round(float(mass), 1)

    if exact:
        # Exact search mode
        matched_element = mass_dict.get(mass)
    else:
        # Closest match mode
        mass_closest = min(mass_dict.keys(), key=lambda k: abs(k - mass))
        msg = "Closest mass to {}: {}".format(mass, mass_closest)
        warnings.warn(msg)
        matched_element = mass_dict.get(mass_closest)

    if matched_element is None:
        raise ElementError(f"No element with mass {mass}")

    if len(matched_element) == 1:
        matched_element = matched_element[0]
    else:
        if duplicates.lower() == "error":
            raise MultiMatchError(
                f"Multiple elements have mass {mass}: {matched_element}"
            )
        elif duplicates.lower() == "all":
            matched_element = tuple(matched_element)
        elif duplicates.lower() == "none":
            matched_element = None

    return matched_element


def infer_element_from_string(string):
    """Attempt to infer an element from a string

    First checks if the string matches a two-character
    element symbol. If not, checks if the string matches
    an element name.

    Parameters
    ----------
    string : str
        String to attempt element inference from

    Returns
    -------
    matched_element : element.Element
        The matching element from the periodic table

    Raises
    ------
    ElementError
        If no match is found
    """
    if not isinstance(string, str):
        raise TypeError(
            f"`string` ({string}) must be a string.  Provided {type(string).__name__}."
        )

    try:
        matched_element = element_from_symbol(string)
    except ElementError:
        try:
            matched_element = element_from_name(string)
        except ElementError:
            raise ElementError(f"Unable to match {string} with element name or symbol")

    return matched_element


elements = []
with open(JSON_PATH) as json_file:
    elements_dict = json.load(json_file)
    elements_dict = {int(key): value for key, value in elements_dict.items()}

for atomic_number, element_properties in elements_dict.items():
    assert atomic_number == element_properties["atomic number"]
    elements.append(
        Element(
            atomic_number=element_properties["atomic number"],
            name=element_properties["name"],
            symbol=element_properties["symbol"],
            mass=element_properties["mass"],
            radius_bondi=element_properties["radius_bondi"],
            radius_alvarez=element_properties["radius_alvarez"],
        )
    )

symbol_dict = {element.symbol: element for element in elements}
name_dict = {element.name: element for element in elements}
atomic_dict = {element.atomic_number: element for element in elements}
mass_dict = {}
for element in elements:
    rounded_mass = round(element.mass, 1)
    if rounded_mass in mass_dict.keys():
        mass_dict[rounded_mass].append(element)
    else:
        mass_dict[rounded_mass] = [element]


class Elements(namedtuple("Elements", "symbols_dict")):
    def __init__(self, symbols_dict):
        super(Elements, self).__init__()
        for key, value in symbols_dict.items():
            setattr(self, key, value)

    def __getattr__(self, item):
        if item not in self.symbols_dict:
            raise AttributeError(
                f'Element with symbol "{item}" does not exist'
            )


Elements = Elements(symbols_dict=symbol_dict)
