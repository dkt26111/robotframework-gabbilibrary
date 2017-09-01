Robot framework test library for gabbi tests
============================================

Overview
--------
**robotframework-gabbilibrary** is a `Robot Framework
<https://github.com/robotframework/robotframework>`_ test library that creates
dynamic keywords out of `gabbi tests <https://github.com/cdent/gabbi>`_
specified in YAML format for consumption in test cases written for Robot Framework.

Installation
------------
To install **robotframework-gabbilibrary**, clone this repo and run::

    python setup.py install

Usage
-----
Include the library in your robot test file:

============  ================  ================  ================================================================
  Setting          Value            Argument        Documentation
============  ================  ================  ================================================================
Library       GabbiLibrary      - url             - url is the URL of the RESTful web service under test
                                - gabbit_path     - gabbit_path is the directory where is gabbi files are located
============  ================  ================  ================================================================

**robotframework-gabbilibrary** will read the gabbi files located under gabbit_path.
It creates dynamic keywords matching the gabbi test names.

Calling Gabbi Test
~~~~~~~~~~~~~~~~~~~~
Each gabbi testcase specified in the gabbi files is loaded as a dynamic keyword
in Robot Framework.

The keywords are called from a robot test suite using optional arguments and
return value as shown below.

+---------------------------------------------------------------------------------+
| **Note:**                                                                       |
|                                                                                 |
| The standard behavior of gabbi to run all tests defined in a single YAML file   |
| has been modified.  Instead when calling a gabbi test from a robot test suite   |
| using **robotframework-gabbilibrary**, only that single gabbi test will be      |
| executed.                                                                       |
+---------------------------------------------------------------------------------+

Gabbi Test Arguments
~~~~~~~~~~~~~~~~~~~~
Arguments can be passed to a dynamic keyword defined in a gabbi tests as a named argument:

=================  ================  ================================================================
   Value            Argument               Documentation
=================  ================  ================================================================
*gabbi test name*   NAME=VALUE       - Creates an environment variable consisting of the specified NAME and VALUE.
                                     - The gabbi test will be able to retrieve the value using $ENVIRON construct.
\                    url=VALUE        - Overwrites the URL of the web service under test with the specified VALUE for this test only.
=================  ================  ================================================================

Gabbi Test Return Values
~~~~~~~~~~~~~~~~~~~~~~~~
**robotframework-gabbilibrary** adds two new response handlers to gabbi for
storing values from the response header or from the response body.  These addtional
keys can be used in the gabbi tests:

===============================  ======================================================================================================================================
   Key                            Description
===============================  ======================================================================================================================================
response_store_value             - A dictionary of a JSONPath rule paired with the name under which to store the retrieved value.
                                 - Returns to Robot Framework a dictionary consisting of the specified name and retrieved value from the JSONPath query.
response_headers_store_value     - A dictionary of key-value pairs consisting of the response header name to retrieve and the name under which to store the retrieved value.
                                 - Returns to Robot Framework a dictionary consisting of the specified name and retrieved value.
===============================  ======================================================================================================================================

Sample Test Suites
~~~~~~~~~~~~~~~~~~
For a sample implementation of a robot testsuite that utilizes
**robotframework-gabbilibrary**, please check
`robotgabbi-openstack <https://github.com/dkt26111/robotgabbi-openstack>`_.
