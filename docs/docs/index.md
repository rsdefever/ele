# Ele

![License: MIT](https://img.shields.io/github/license/rsdefever/ele)
[![Build Status](https://dev.azure.com/rdefever/ele/_apis/build/status/rsdefever.ele?branchName=master)](https://dev.azure.com/rdefever/ele/_apis/build/status/rsdefever.ele?branchName=master)
![CodeCov](https://codecov.io/gh/rsdefever/ele/branch/master/graph/badge.svg)

## Overview

**Ele**ment is an extremely lightweight package that defines
the elements of the periodic table and allows them to be accessed
by symbol, name, atomic number, or mass. It has *zero dependencies*
outside of the Python Standard Library.

## Warning

**Ele** is still in early development (0.x releases). The API may
change unexpectedly.

## Usage

**Ele** only supports a few modes of use. You can retrieve an element
from the symbol, the name, the atomic number, or the mass (in amu):

	import ele
	na = ele.element_from_symbol("Na")
	na = ele.element_from_name("sodium")
	na = ele.element_from_atomic_number(11)
	na = ele.element_from_mass(22.990)


The mass is rounded to a single decimal before comparison. If you wish to
retrieve the element with the mass closest to the specified value you
may use the `exact=False` keyword.

Each `Element` has four attributes which can be accessed
(as demonstrated below for ``na``):

	na.name
	na.symbol
	na.atomic_number
	na.mass


The elements can also be accessed by symbol as follows:

	import ele
	na = ele.Elements.Na


## Installation


Install is supported through pip:

	pip install ele

and conda:

	conda install -c conda-forge ele


Complete installation instructions can be found [here](install.md).


## Data Sources

We have compiled the atomic weights in a systematic fashion. Complete details of the data sources are provided [here](sources.md).


## Credits

Development of Ele was supported by the National Science Foundation
under grant NSF Grant Number 1835874. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the author(s) and do
not necessarily reflect the views of the National Science Foundation.
