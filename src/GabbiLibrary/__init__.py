import sys
import os
import unittest

from gabbi import driver

import handlers
import testrunner


class GabbiLibrary(object):
    """Test library for Robot Framework implementing test cases in Gabbi
    test files

    """

    def __init__(self, url, gabbit_path):
        self.testcases = {}
        self.url = url
        self.gabbit_path = str(gabbit_path)

    def _build_gabbi_testsuite(self, url_override=None):
        # build gabbi test suite
        top_testsuite = \
            driver.build_tests(self.gabbit_path,
                               unittest.TestLoader(),
                               host='localhost',
                               response_handlers=[
                                   handlers.StoreHeadersResponseHandler],
                               content_handlers=[
                                   handlers.StoreResponseValueHandler],
                               url=url_override if url_override else self.url,
                               test_loader_name='dummy',
                               use_prior_test=False)

        # save each testcase name and object in dictionary
        for testsuite in top_testsuite:
            for tc in testsuite:
                # strip out filename prefix
                filename, method = type(tc).__name__.split('_', 1)
                self.testcases[method] = tc

    def get_keyword_names(self):
        self._build_gabbi_testsuite()
        return list(self.testcases.keys())

    def run_keyword(self, name, args, keywords):
        print "Running keyword '%s' with arguments %s and keywords %s." % \
              (name, args, keywords)

        # overwrite url for this testcase if specified
        url = None
        if 'url' in keywords:
            url = keywords['url']

        self._build_gabbi_testsuite(url)
        if name in self.testcases and self.testcases[name]:
            # create suite that contains single testcase
            suite = unittest.TestSuite()
            suite.addTest(self.testcases[name])

            # set keyword arguments as environment variables
            for k, v in keywords.iteritems():
                print "Setting env var %s to %s" % (k, v)
                os.environ[k] = v

            # run suite and raise error if testcase failed
            result = testrunner.GabbiTestRunner(sys.stdout).run(suite)
            if not result.wasSuccessful():
                raise AssertionError('Testcase ' + name + ' failed.')

            # return any stored value back to Robot
            return result.response_values
