"""
Cookie Clicker Simulator
"""

import simpleplot
import math
import SimpleGUICS2Pygame.codeskulptor as codeskulptor
import poc_clicker_provided as provided

# Used to increase the timeout, if necessary
codeskulptor.set_timeout(20)

# Constants
SIM_TIME = 10000000000.0


class ClickerState:
    """
    Simple class to keep track of the game state.
    """

    def __init__(self, total_cookies=0, current_cookies=0, current_seconds=0, current_cps=1):
        self._total_cookies = total_cookies
        self._current_cookies = current_cookies
        self._current_seconds = current_seconds
        self._current_cps = current_cps
        self._history = []
        self._update_history(self._current_seconds, None, 0.0, self._total_cookies)

    def __str__(self):
        """
        Return human readable state
        """
        clicker_state_dict = {}

        for attribute, value in self.__dict__.items():
            clicker_state_dict[attribute.strip('_')] = value

        return str(clicker_state_dict)

    def _update_history(self, time, item, cost_item, total_cookies):
        self._history.append((time, item, cost_item, total_cookies))

    def get_cookies(self):
        """
        Return current number of cookies
        (not total number of cookies)

        Should return a float
        """
        return self._current_cookies

    def get_cps(self):
        """
        Get current CPS

        Should return a float
        """
        return self._current_cps

    def get_time(self):
        """
        Get current time

        Should return a float
        """
        return self._current_seconds

    def get_history(self):
        """
        Return history list

        History list should be a list of tuples of the form:
        (time, item, cost of item, total cookies)

        For example: [(0.0, None, 0.0, 0.0)]

        Should return a copy of any internal data structures,
        so that they will not be modified outside of the class.
        """
        history_copy = self._history[:]

        return history_copy

    def time_until(self, cookies):
        """
        Return time until you have the given number of cookies
        (could be 0.0 if you already have enough cookies)

        Should return a float with no fractional part
        """
        time = 0.0

        if self._current_cookies < cookies:
            time = math.ceil((cookies - self._current_cookies) / float(self._current_cps))

        return time

    def wait(self, time):
        """
        Wait for given amount of time and update state

        Should do nothing if time <= 0.0
        """
        time = int(time)
        self._current_seconds += time
        stored_cookies = time * self._current_cps
        self._current_cookies += stored_cookies
        self._total_cookies += stored_cookies

    def buy_item(self, item_name, cost, additional_cps):
        """
        Buy an item and update state

        Should do nothing if you cannot afford the item
        """
        if cost <= self._current_cookies:
            self._current_cookies -= cost
            self._current_cps += additional_cps
            self._update_history(self._current_seconds, item_name, cost, self._total_cookies)

        return


def simulate_clicker(build_info, duration, strategy):
    """
    Function to run a Cookie Clicker game for the given
    duration with the given strategy.  Returns a ClickerState
    object corresponding to the final state of the game.
    """

    # Replace with your code
    build_info_object_cloned = build_info.clone()
    state = ClickerState()

    while state.get_time() < duration:
        current_cookies = state.get_cookies()
        current_cps = state.get_cps()
        history = state.get_history()
        time_left = duration - state.get_time()

        item_to_buy = strategy(current_cookies, current_cps, history, time_left, build_info_object_cloned)
        if item_to_buy is None:
            break

        time_to_buy = state.time_until(build_info_object_cloned.get_cost(item_to_buy))
        if duration < (state.get_time() + time_to_buy):
            break

        state.wait(time_to_buy)
        state.buy_item(item_to_buy, build_info_object_cloned.get_cost(item_to_buy),
                       build_info_object_cloned.get_cps(item_to_buy))
        build_info_object_cloned.update_item(item_to_buy)

    state.wait(duration - state.get_time())

    return state


def strategy_cursor_broken(cookies, cps, history, time_left, build_info):
    """
    Always pick Cursor!

    Note that this simplistic (and broken) strategy does not properly
    check whether it can actually buy a Cursor in the time left.  Your
    simulate_clicker function must be able to deal with such broken
    strategies.  Further, your strategy functions must correctly check
    if you can buy the item in the time left and return None if you
    can't.
    """
    return "Cursor"


def strategy_none(cookies, cps, history, time_left, build_info):
    """
    Always return None

    This is a pointless strategy that will never buy anything, but
    that you can use to help debug your simulate_clicker function.
    """
    return None


def strategy_cheap(cookies, cps, history, time_left, build_info):
    """
    Always buy the cheapest item you can afford in the time left.
    """
    state = ClickerState(cookies, 0, 0, cps)
    state.wait(time_left)
    cookies += state.get_cookies()
    cheapest = build_info.build_items()[0]
    for item in build_info.build_items():
        if cookies >= build_info.get_cost(item):
            cheapest = item
            break
        else:
            return None

    for item in build_info.build_items():
        if cookies >= build_info.get_cost(item) < build_info.get_cost(cheapest):
            cheapest = item

    return cheapest


def strategy_expensive(cookies, cps, history, time_left, build_info):
    """
    Always buy the most expensive item you can afford in the time left.
    """
    return None


def strategy_best(cookies, cps, history, time_left, build_info):
    """
    The best strategy that you are able to implement.
    """
    return None


def run_strategy(strategy_name, time, strategy):
    """
    Run a simulation for the given time with one strategy.
    """
    state = simulate_clicker(provided.BuildInfo(), time, strategy)
    print strategy_name, ":", state

    # Plot total cookies over time

    # Uncomment out the lines below to see a plot of total cookies vs. time
    # Be sure to allow popups, if you do want to see it

    # history = state.get_history()
    # history = [(item[0], item[3]) for item in history]
    # simpleplot.plot_lines(strategy_name, 1000, 400, 'Time', 'Total Cookies', [history], True)


def run():
    """
    Run the simulator.
    """
    # run_strategy("Cursor", SIM_TIME, strategy_cursor_broken)

    # Add calls to run_strategy to run additional strategies
    run_strategy("Cheap", SIM_TIME, strategy_cheap)
    # run_strategy("Expensive", SIM_TIME, strategy_expensive)
    # run_strategy("Best", SIM_TIME, strategy_best)


# todo: remove before Owltest
run()
