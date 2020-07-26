import warnings
from re import sub

from collections import namedtuple

from element.exceptions import ElementError


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
Hydrogen = Element(atomic_number=1, name="hydrogen", symbol="H", mass=1.0079)
Helium = Element(atomic_number=2, name="helium", symbol="He", mass=4.0026)
Lithium = Element(atomic_number=3, name="lithium", symbol="Li", mass=6.941)
Beryllium = Element(
    atomic_number=4, name="beryllium", symbol="Be", mass=9.0122
)
Boron = Element(atomic_number=5, name="boron", symbol="B", mass=10.811)
Carbon = Element(atomic_number=6, name="carbon", symbol="C", mass=12.0107)
Nitrogen = Element(atomic_number=7, name="nitrogen", symbol="N", mass=14.0067)
Oxygen = Element(atomic_number=8, name="oxygen", symbol="O", mass=15.9994)
Fluorine = Element(atomic_number=9, name="fluorine", symbol="F", mass=18.9984)
Neon = Element(atomic_number=10, name="neon", symbol="Ne", mass=20.1797)
Sodium = Element(atomic_number=11, name="sodium", symbol="Na", mass=22.9898)
Magnesium = Element(
    atomic_number=12, name="magnesium", symbol="Mg", mass=24.305
)
Aluminum = Element(
    atomic_number=13, name="aluminum", symbol="Al", mass=26.9815
)
Silicon = Element(atomic_number=14, name="silicon", symbol="Si", mass=28.0855)
Phosphorus = Element(
    atomic_number=15, name="phosphorus", symbol="P", mass=30.9738
)
Sulfur = Element(atomic_number=16, name="sulfur", symbol="S", mass=32.065)
Chlorine = Element(atomic_number=17, name="chlorine", symbol="Cl", mass=35.453)
Argon = Element(atomic_number=18, name="argon", symbol="Ar", mass=39.948)
Potassium = Element(
    atomic_number=19, name="potassium", symbol="K", mass=39.0983
)
Calcium = Element(atomic_number=20, name="calcium", symbol="Ca", mass=40.078)
Scandium = Element(
    atomic_number=21, name="scandium", symbol="Sc", mass=44.9559
)
Titanium = Element(atomic_number=22, name="titanium", symbol="Ti", mass=47.867)
Vanadium = Element(atomic_number=23, name="vanadium", symbol="V", mass=50.9415)
Chromium = Element(
    atomic_number=24, name="chromium", symbol="Cr", mass=51.9961
)
Manganese = Element(
    atomic_number=25, name="manganese", symbol="Mn", mass=54.938
)
Iron = Element(atomic_number=26, name="iron", symbol="Fe", mass=55.845)
Cobalt = Element(atomic_number=27, name="cobalt", symbol="Co", mass=58.9331)
Nickel = Element(atomic_number=28, name="nickel", symbol="Ni", mass=58.6934)
Copper = Element(atomic_number=29, name="copper", symbol="Cu", mass=63.546)
Zinc = Element(atomic_number=30, name="zinc", symbol="Zn", mass=65.409)
Gallium = Element(atomic_number=31, name="gallium", symbol="Ga", mass=69.723)
Germanium = Element(
    atomic_number=32, name="germanium", symbol="Ge", mass=72.64
)
Arsenic = Element(atomic_number=33, name="arsenic", symbol="As", mass=74.9216)
Selenium = Element(atomic_number=34, name="selenium", symbol="Se", mass=78.96)
Bromine = Element(atomic_number=35, name="bromine", symbol="Br", mass=79.904)
Krypton = Element(atomic_number=36, name="krypton", symbol="Kr", mass=83.798)
Rubidium = Element(
    atomic_number=37, name="rubidium", symbol="Rb", mass=85.4678
)
Strontium = Element(
    atomic_number=38, name="strontium", symbol="Sr", mass=87.62
)
Yttrium = Element(atomic_number=39, name="yttrium", symbol="Y", mass=88.9059)
Zirconium = Element(
    atomic_number=40, name="zirconium", symbol="Zr", mass=91.224
)
Niobium = Element(atomic_number=41, name="niobium", symbol="Nb", mass=92.9064)
Molybdenum = Element(
    atomic_number=42, name="molybdenum", symbol="Mo", mass=95.94
)
Technetium = Element(
    atomic_number=43, name="technetium", symbol="Tc", mass=98.0
)
Ruthenium = Element(
    atomic_number=44, name="ruthenium", symbol="Ru", mass=101.07
)
Rhodium = Element(atomic_number=45, name="rhodium", symbol="Rh", mass=102.9055)
Palladium = Element(
    atomic_number=46, name="palladium", symbol="Pd", mass=106.42
)
Silver = Element(atomic_number=47, name="silver", symbol="Ag", mass=107.8682)
Cadmium = Element(atomic_number=48, name="cadmium", symbol="Cd", mass=112.411)
Indium = Element(atomic_number=49, name="indium", symbol="In", mass=114.818)
Tin = Element(atomic_number=50, name="tin", symbol="Sn", mass=118.71)
Antimony = Element(atomic_number=51, name="antimony", symbol="Sb", mass=121.76)
Tellurium = Element(
    atomic_number=52, name="tellurium", symbol="Te", mass=127.6
)
Iodine = Element(atomic_number=53, name="iodine", symbol="I", mass=126.9045)
Xenon = Element(atomic_number=54, name="xenon", symbol="Xe", mass=131.293)
Cesium = Element(atomic_number=55, name="cesium", symbol="Cs", mass=132.9055)
Barium = Element(atomic_number=56, name="barium", symbol="Ba", mass=137.327)
Lanthanum = Element(
    atomic_number=57, name="lanthanum", symbol="La", mass=138.9055
)
Cerium = Element(atomic_number=58, name="cerium", symbol="Ce", mass=140.116)
Praseodymium = Element(
    atomic_number=59, name="praseodymium", symbol="Pr", mass=140.9077
)
Neodymium = Element(
    atomic_number=60, name="neodymium", symbol="Nd", mass=144.242
)
Promethium = Element(
    atomic_number=61, name="promethium", symbol="Pm", mass=145.0
)
Samarium = Element(atomic_number=62, name="samarium", symbol="Sm", mass=150.36)
Europium = Element(
    atomic_number=63, name="europium", symbol="Eu", mass=151.964
)
Gadolinium = Element(
    atomic_number=64, name="gadolinium", symbol="Gd", mass=157.25
)
Terbium = Element(atomic_number=65, name="terbium", symbol="Tb", mass=158.9254)
Dysprosium = Element(
    atomic_number=66, name="dysprosium", symbol="Dy", mass=162.5
)
Holmium = Element(atomic_number=67, name="holmium", symbol="Ho", mass=164.9303)
Erbium = Element(atomic_number=68, name="erbium", symbol="Er", mass=167.259)
Thulium = Element(atomic_number=69, name="thulium", symbol="Tm", mass=168.9342)
Ytterbium = Element(
    atomic_number=70, name="ytterbium", symbol="Yb", mass=173.04
)
Lutetium = Element(
    atomic_number=71, name="lutetium", symbol="Lu", mass=174.967
)
Hafnium = Element(atomic_number=72, name="hafnium", symbol="Hf", mass=178.49)
Tantalum = Element(
    atomic_number=73, name="tantalum", symbol="Ta", mass=180.9479
)
Tungsten = Element(atomic_number=74, name="tungsten", symbol="W", mass=183.84)
Rhenium = Element(atomic_number=75, name="rhenium", symbol="Re", mass=186.207)
Osmium = Element(atomic_number=76, name="osmium", symbol="Os", mass=190.23)
Iridium = Element(atomic_number=77, name="iridium", symbol="Ir", mass=192.217)
Platinum = Element(
    atomic_number=78, name="platinum", symbol="Pt", mass=195.084
)
Gold = Element(atomic_number=79, name="gold", symbol="Au", mass=196.9666)
Mercury = Element(atomic_number=80, name="mercury", symbol="Hg", mass=200.59)
Thallium = Element(
    atomic_number=81, name="thallium", symbol="Tl", mass=204.3833
)
Lead = Element(atomic_number=82, name="lead", symbol="Pb", mass=207.2)
Bismuth = Element(atomic_number=83, name="bismuth", symbol="Bi", mass=208.9804)
Polonium = Element(atomic_number=84, name="polonium", symbol="Po", mass=209.0)
Astatine = Element(atomic_number=85, name="astatine", symbol="At", mass=210.0)
Radon = Element(atomic_number=86, name="radon", symbol="Rn", mass=222.0)
Francium = Element(atomic_number=87, name="francium", symbol="Fr", mass=223.0)
Radium = Element(atomic_number=88, name="radium", symbol="Ra", mass=226.0)
Actinium = Element(atomic_number=89, name="actinium", symbol="Ac", mass=227.0)
Thorium = Element(atomic_number=90, name="thorium", symbol="Th", mass=232.0381)
Proactinium = Element(
    atomic_number=91, name="proactinium", symbol="Pa", mass=231.0359
)
Uranium = Element(atomic_number=92, name="uranium", symbol="U", mass=238.0289)
Neptunium = Element(
    atomic_number=93, name="neptunium", symbol="Np", mass=237.0
)
Plutonium = Element(
    atomic_number=94, name="plutonium", symbol="Pu", mass=244.0
)
Americium = Element(
    atomic_number=95, name="americium", symbol="Am", mass=243.0
)
Curium = Element(atomic_number=96, name="curium", symbol="Cm", mass=247.0)
Berkelium = Element(
    atomic_number=97, name="berkelium", symbol="Bk", mass=247.0
)
Californium = Element(
    atomic_number=98, name="californium", symbol="Cf", mass=251.0
)
Einsteinium = Element(
    atomic_number=99, name="einsteinium", symbol="Es", mass=252.0
)
Fermium = Element(atomic_number=100, name="fermium", symbol="Fm", mass=257.0)
Mendelevium = Element(
    atomic_number=101, name="mendelevium", symbol="Md", mass=258.0
)
Nobelium = Element(atomic_number=102, name="nobelium", symbol="No", mass=259.0)
Lawrencium = Element(
    atomic_number=103, name="lawrencium", symbol="Lr", mass=262.0
)
Rutherfordium = Element(
    atomic_number=104, name="rutherfordium", symbol="Rf", mass=261.0
)
Dubnium = Element(atomic_number=105, name="dubnium", symbol="Db", mass=262.0)
Seaborgium = Element(
    atomic_number=106, name="seaborgium", symbol="Sg", mass=266.0
)
Bohrium = Element(atomic_number=107, name="bohrium", symbol="Bh", mass=264.0)
Hassium = Element(atomic_number=108, name="hassium", symbol="Hs", mass=277.0)
Meitnerium = Element(
    atomic_number=109, name="meitnerium", symbol="Mt", mass=268.0
)
Darmstadtium = Element(
    atomic_number=110, name="darmstadtium", symbol="Ds", mass=281.0
)
Roentgenium = Element(
    atomic_number=111, name="roentgenium", symbol="Rg", mass=272.0
)
Copernicium = Element(
    atomic_number=112, name="copernicium", symbol="Cn", mass=285.0
)
Ununtrium = Element(
    atomic_number=113, name="ununtrium", symbol="Uut", mass=284.0
)
Ununquadium = Element(
    atomic_number=114, name="ununquadium", symbol="Uuq", mass=289.0
)
Ununpentium = Element(
    atomic_number=115, name="ununpentium", symbol="Uup", mass=288.0
)
Ununhexium = Element(
    atomic_number=116, name="ununhexium", symbol="Uuh", mass=292.0
)
Ununseptium = Element(
    atomic_number=117, name="ununseptium", symbol="Uus", mass=291.0
)
Ununoctium = Element(
    atomic_number=118, name="ununoctium", symbol="Uuo", mass=294.0
)

elements = [
    Hydrogen,
    Helium,
    Lithium,
    Beryllium,
    Boron,
    Carbon,
    Nitrogen,
    Oxygen,
    Fluorine,
    Neon,
    Sodium,
    Magnesium,
    Aluminum,
    Silicon,
    Phosphorus,
    Sulfur,
    Chlorine,
    Argon,
    Potassium,
    Calcium,
    Scandium,
    Titanium,
    Vanadium,
    Chromium,
    Manganese,
    Iron,
    Cobalt,
    Nickel,
    Copper,
    Zinc,
    Gallium,
    Germanium,
    Arsenic,
    Selenium,
    Bromine,
    Krypton,
    Rubidium,
    Strontium,
    Yttrium,
    Zirconium,
    Niobium,
    Molybdenum,
    Technetium,
    Ruthenium,
    Rhodium,
    Palladium,
    Silver,
    Cadmium,
    Indium,
    Tin,
    Antimony,
    Tellurium,
    Iodine,
    Xenon,
    Cesium,
    Barium,
    Lanthanum,
    Cerium,
    Praseodymium,
    Neodymium,
    Promethium,
    Samarium,
    Europium,
    Gadolinium,
    Terbium,
    Dysprosium,
    Holmium,
    Erbium,
    Thulium,
    Ytterbium,
    Lutetium,
    Hafnium,
    Tantalum,
    Tungsten,
    Rhenium,
    Osmium,
    Iridium,
    Platinum,
    Gold,
    Mercury,
    Thallium,
    Lead,
    Bismuth,
    Polonium,
    Astatine,
    Radon,
    Francium,
    Radium,
    Actinium,
    Thorium,
    Proactinium,
    Uranium,
    Neptunium,
    Plutonium,
    Americium,
    Curium,
    Berkelium,
    Californium,
    Einsteinium,
    Fermium,
    Mendelevium,
    Nobelium,
    Lawrencium,
    Rutherfordium,
    Dubnium,
    Seaborgium,
    Bohrium,
    Hassium,
    Meitnerium,
    Darmstadtium,
    Roentgenium,
    Copernicium,
    Ununtrium,
    Ununquadium,
    Ununpentium,
    Ununhexium,
    Ununseptium,
    Ununoctium,
]

symbol_dict = {element.symbol: element for element in elements}
name_dict = {element.name: element for element in elements}
atomic_dict = {element.atomic_number: element for element in elements}
mass_dict = {round(element.mass, 1): element for element in elements}
