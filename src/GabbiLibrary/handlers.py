from gabbi.handlers import core
from gabbi.handlers import jsonhandler


class StoreResponseValueHandler(jsonhandler.JSONHandler):
    """Store value in response to be returned to Robot Framework

    Based on JSONHandler in gabbi tool
    """

    test_key_suffix = 'store_value'
    test_key_value = {}

    def action(self, test, path, value=None):
        path = test.replace_template(path)
        try:
            match = self.extract_json_path_value(
                test.response_data, path)
        except AttributeError:
            raise AssertionError('unable to extract JSON from test results')
        except ValueError:
            raise AssertionError('json path %s cannot match %s' %
                                 (path, test.response_data))

        test.result.add_response_value(value, match)


class StoreHeadersResponseHandler(core.HeadersResponseHandler):
    """Store value in response header to be returned to Robot Framework

    Based on ResponseHandler in gabbi tool
    """

    test_key_suffix = 'headers_store_value'
    test_key_value = {}

    def action(self, test, header, value=None):
        header = header.lower()  # case-insensitive comparison

        response = test.response

        try:
            response_value = str(response[header])
        except KeyError:
            raise AssertionError(
                "'%s' header not present in response: %s" %
                (header, response.keys()))

        test.result.add_response_value(value, str(response_value))
