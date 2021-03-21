"""
Lightweight testing class inspired by unittest from Pyunit
https://docs.python.org/2/library/unittest.html
Note that code is designed to be much simpler than unittest
and does NOT replicate unittest functionality
"""
import Yahtzee


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


def run_suite(format_function):
    """
    Some informal testing code
    """

    # create a TestSuite object
    suite = TestSuite()
    num_die_sides = 6

    # test format_function on various inputs
    suite.run_test(format_function((1, 1), num_die_sides), (5.055555555555555, ()), "Test #1:")
    suite.run_test(format_function((1, 2), num_die_sides), (5.055555555555555, ()), "Test #2:")
    suite.run_test(format_function((1, 3), num_die_sides), (5.055555555555555, ()), "Test #3:")
    suite.run_test(format_function((1, 4), num_die_sides), (5.166666666666667, (4,)), "Test #4:")
    suite.run_test(format_function((1, 5), num_die_sides), (6.0, (5,)), "Test #5:")
    suite.run_test(format_function((1, 6), num_die_sides), (7.0, (6,)), "Test #6:")

    suite.run_test(format_function((1, 1), num_die_sides), (5.055555555555555, ()), "Test #7:")
    suite.run_test(format_function((2, 2), num_die_sides), (5.055555555555555, ()), "Test #8:")
    suite.run_test(format_function((3, 3), num_die_sides), (6.0, (3, 3)), "Test #9:")
    suite.run_test(format_function((4, 4), num_die_sides), (8.0, (4, 4)), "Test #10:")
    suite.run_test(format_function((5, 5), num_die_sides), (10.0, (5, 5)), "Test #11:")
    suite.run_test(format_function((6, 6), num_die_sides), (12.0, (6, 6)), "Test #12:")

    suite.run_test(format_function((1, 6), num_die_sides), (7.0, (6,)), "Test #13:")
    suite.run_test(format_function((2, 6), num_die_sides), (7.0, (6,)), "Test #14:")
    suite.run_test(format_function((3, 6), num_die_sides), (7.0, (6,)), "Test #15:")
    suite.run_test(format_function((4, 6), num_die_sides), (7.0, (6,)), "Test #16:")
    suite.run_test(format_function((5, 6), num_die_sides), (7.0, (6,)), "Test #17:")
    suite.run_test(format_function((6, 6), num_die_sides), (12.0, (6, 6)), "Test #18:")

    suite.report_results()


run_suite(Yahtzee.strategy)
