
Element
=======
|License|
|CodeCov|
|Azure|

.. |Codecov| image:: https://codecov.io/gh/rsdefever/element/branch/master/graph/badge.svg
.. |Azure| image:: https://dev.azure.com/rdefever/element/_apis/build/status/rsdefever.element?branchName=master
.. |License| image:: https://img.shields.io/github/license/rsdefever/element

Overview
~~~~~~~~

**Element** is an extremely lightweight package that defines
the elements of the periodic table and allows them to be accessed
by symbol, name, atomic number, or mass. It has *zero dependencies*
outside of the Python Standard Library.

Warning
~~~~~~~

**Element** is still in early development (0.x releases). The API may
change unexpectedly.

Usage
~~~~~

**Element** only supports a few modes of use. You can retrieve an element
from the symbol, the name, the atomic number, or the mass (in amu):

.. code-block:: python

  import element
  na = element.element_from_symbol("Na")
  na = element.element_from_name("sodium")
  na = element.element_from_atomic_number(11)
  na = element.element_from_mass(22.989)

The mass is rounded to a single decimal before comparison. If you wish to
retrieve the element with the mass closest to the specified value you
may use the ``exact=False`` keyword.

Each ``Element`` has four attributes which can be accessed
(as demonstrated below for ``na``):

.. code-block:: python

  na.name
  na.symbol
  na.atomic_number
  na.mass

The elements can also be accessed by symbol as follows:

.. code-block:: python

  import element
  na = element.Elements.Na

Resources
~~~~~~~~~

Installation
~~~~~~~~~~~~

Installation is currently limited to source:

.. code-block:: bash
  
  git clone git@github.com/rsdefever/element.git
  cd element
  pip install .

``pip`` and ``conda`` installations are coming soon!

Credits
~~~~~~~

Development of Element was supported by the National Science Foundation
under grant NSF Grant Number 1835874. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the author(s) and do
not necessarily reflect the views of the National Science Foundation.
