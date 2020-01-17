========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |actions| |dependabot|
        | |codecov|
.. |docs| image:: https://readthedocs.org/projects/erddap-xml-validator/badge/?version=latest
    :target: https://erddap-xml-validator.readthedocs.io/en/latest/
    :alt: Documentation Status

.. |actions| image:: https://github.com/gulfofmaine/python-erddap-xml-validator/workflows/Push/badge.svg
    :alt: Github Actions Build Status

.. |dependabot| image:: https://api.dependabot.com/badges/status?host=github&repo=gulfofmaine/python-erddap-xml-validator
    :alt: Dependabot dependency management

.. |codecov| image:: permanently to https://codecov.io/gh/gulfofmaine/python-erddap-xml-validator/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/gulfofmaine/python-erddap-xml-validator

.. end-badges

Validate ERDDAP XML files and snippets to make sure they conform to best practices.

* Free software: MIT license

Installation
============

::

    pip install erddap-xml

You can also install the in-development version with::

    pip install https://github.com/gulfofmaine/python-erddap-xml-validator/archive/master.zip




Documentation
=============


`Read the docs <https://erddap-xml-validator.readthedocs.io/>`_

``erddap_xml`` can be imported into a larger project, and can be used from the command line.

``erddap_xml_validate path/to/dataset.xml`` will check if an XML chunk for a single dataset is
correctly formatted. It will print ``Valid Dataset`` if it's correctly formatted, or raise an
exception pointing to the specific check that the dataset failed.


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
