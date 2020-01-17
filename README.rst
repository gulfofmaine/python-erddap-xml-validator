========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
        | |codacy|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/python-erddap-xml-validator/badge/?style=flat
    :target: https://readthedocs.org/projects/python-erddap-xml-validator
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/gulfofmaine/python-erddap-xml-validator.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/gulfofmaine/python-erddap-xml-validator

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/gulfofmaine/python-erddap-xml-validator?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/gulfofmaine/python-erddap-xml-validator

.. |requires| image:: https://requires.io/github/gulfofmaine/python-erddap-xml-validator/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/gulfofmaine/python-erddap-xml-validator/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/gulfofmaine/python-erddap-xml-validator/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/gulfofmaine/python-erddap-xml-validator

.. |codacy| image:: https://img.shields.io/codacy/grade/[Get ID from https://app.codacy.com/app/gulfofmaine/python-erddap-xml-validator/settings].svg
    :target: https://www.codacy.com/app/gulfofmaine/python-erddap-xml-validator
    :alt: Codacy Code Quality Status

.. |version| image:: https://img.shields.io/pypi/v/erddap-xml.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/erddap-xml

.. |wheel| image:: https://img.shields.io/pypi/wheel/erddap-xml.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/erddap-xml

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/erddap-xml.svg
    :alt: Supported versions
    :target: https://pypi.org/project/erddap-xml

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/erddap-xml.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/erddap-xml

.. |commits-since| image:: https://img.shields.io/github/commits-since/gulfofmaine/python-erddap-xml-validator/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/gulfofmaine/python-erddap-xml-validator/compare/v0.0.0...master



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


erddap-xml.readthedocs.io


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
