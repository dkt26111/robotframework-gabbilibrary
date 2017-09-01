import unittest


class _GabbiTestResult(unittest._TextTestResult):
    """Custom test result for Gabbi test cases

    Provides method to store value extracted from response header or body
    """

    def __init__(self, stream, descriptions, verbosity):
        unittest._TextTestResult.__init__(self, stream, descriptions,
                                          verbosity)
        self.response_values = {}

    def add_response_value(self, key, value):
        self.response_values[key] = value


class GabbiTestRunner(unittest.TextTestRunner):
    """Custom test runner for Gabbi test cases

    Overloads unittest TextTestRunner makeResult to use _GabbiTestResult
    """

    def _makeResult(self):
        return _GabbiTestResult(self.stream, self.descriptions, self.verbosity)
