"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
from game_2048 import merge


class TestSuite:
    """
    Create a suite of tests similar to unittest
    """

    def __init__(self):
        """
        Creates a test suite object
        """
        self.total_tests = 0
        self.failures = 0

    def run_test(self, computed, expected, message=""):
        """
        Compare computed and expected
        If not equal, print message, computed, expected
        """
        self.total_tests += 1
        if computed != expected:
            msg = message + " Computed: " + str(computed)
            msg += " Expected: " + str(expected)
            print msg
            self.failures += 1

    def report_results(self):
        """
        Report back summary of successes and failures
        from run_test()
        """
        msg = "Ran " + str(self.total_tests) + " tests. "
        msg += str(self.failures) + " failures."
        print msg


def run_suite(testing_func):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = TestSuite()

    # test format_function on various inputs
    suite.run_test(testing_func([1, 2, 3]), [1, 2, 3], "Test #1:")
    suite.run_test(testing_func([2, 0, 2, 4]), [4, 4, 0, 0], "Test #2:")
    suite.run_test(testing_func([0, 0, 2, 2]), [4, 0, 0, 0], "Test #3:")
    suite.run_test(testing_func([2, 2, 0, 0]), [4, 0, 0, 0], "Test #4:")
    suite.run_test(testing_func([2, 2, 2, 2, 2]), [4, 4, 2, 0, 0], "Test #5:")
    suite.run_test(testing_func([8, 16, 16, 8]), [8, 32, 8, 0], "Test #6:")

    suite.report_results()


run_suite(merge)
