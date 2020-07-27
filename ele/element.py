import json
from enum import Enum, unique
import warnings

from collections import namedtuple
from pathlib import Path

from ele.exceptions import ElementError

JSON_PATH = Path.joinpath(Path(__file__).parent, 'lib/elements.json')

class Element(namedtuple("Element", "atomic_number, name, symbol, mass")):
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


def element_from_symbol(symbol):
    """Search for an element by its symbol

    Look up an element from a list of known elements by symbol.
    Return None if no match found.

    Parameters
    ----------
    symbol : str
        Element symbol

    Returns
    -------
    matched_element : element.Element
        Return an element from the periodic table if the symbol is found,
        otherwise return None
    """
    if not isinstance(symbol, str):
        raise TypeError("`symbol` ({symbol}) must be a string")

    symbol = symbol.capitalize()
    matched_element = symbol_dict.get(symbol)
    if matched_element is None:
        raise ElementError(f"No element with symbol {symbol}")

    return matched_element


def element_from_name(name):
    """Search for an element by its name

    Look up an element from a list of known elements by name.
    Return None if no match found.

    Parameters
    ----------
    name : str
        Element name to look for, digits and spaces are removed before search

    Returns
    -------
    matched_element : element.Element
        Return an element from the periodic table if the name is found,
        otherwise return None
    """
    if not isinstance(name, str):
        raise TypeError("`name` ({name}) must be a string")

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
        Return an element from the periodic table if we find a match,
    """
    if not isinstance(atomic_number, int):
        raise TypeError("`atomic_number` ({atomic_number}) must be an int")

    matched_element = atomic_dict.get(atomic_number)
    if matched_element is None:
        raise ElementError(f"No element with atomic number {atomic_number}")

    return matched_element


def element_from_mass(mass, exact=True):
    """Search for an element by its mass

    Look up an element from a list of known elements by mass (amu).

    Parameters
    ----------
    mass : int, float
        Element mass in amu
    exact : bool, optional,  default=True
        Require that the mass match to the first decimal. If False, the
        element with the closest mass will be returned

    Returns
    -------
    matched_element : element.Element
        Return an element from the periodict table if we find a match,
        otherwise return None
    """
    if not isinstance(mass, (float, int)):
        raise TypeError("`mass` ({mass}) must be a float")

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

    return matched_element


# RSD TODO: Where did these values come from???
elements = []
with open(JSON_PATH) as json_file:
    elements_dict = json.load(json_file)

for element_name, element_properties in elements_dict.items():
    elements.append(
        Element(
            atomic_number=element_properties["atomic number"],
            name=element_properties["name"],
            symbol=element_properties["symbol"],
            mass=element_properties["mass"],
        )
    )

symbol_dict = {element.symbol: element for element in elements}
name_dict = {element.name: element for element in elements}
atomic_dict = {element.atomic_number: element for element in elements}
mass_dict = {round(element.mass, 1): element for element in elements}


class Elements(namedtuple('Elements', 'symbols_dict')):
    def __init__(self, symbols_dict):
        super(Elements, self).__init__()
        for key, value in symbols_dict.items():
            setattr(self, key, value)

    def __getattr__(self, item):
        if item not in self.symbols_dict:
            raise AttributeError(f'Element with symbol "{item}" does not exist')


Elements = Elements(symbols_dict=symbol_dict)
