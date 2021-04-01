"""
Simulator for greedy boss scenario
"""

import simpleplot
import math
import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000


def greedy_boss(days_in_simulation, bribe_cost_increment, plot_type=STANDARD):
    """
    Simulation of greedy boss
    """

    bribe = INITIAL_BRIBE_COST
    days_vs_earnings = []
    current_day = 0
    salary = INITIAL_SALARY
    current_savings = 0
    total_salary_earned = 0

    while current_day <= days_in_simulation:

        if plot_type == STANDARD:
            days_vs_earnings.append((current_day, total_salary_earned))
        else:
            if current_day == 0 or total_salary_earned == 0:
                days_vs_earnings.append([math.log(1), math.log(1)])
            else:
                days_vs_earnings.append([math.log(current_day), math.log(total_salary_earned)])

        if current_savings >= bribe:
            days_to_next_bribe = 0
        else:
            days_to_next_bribe = int(math.ceil((bribe - current_savings) / float(salary)))

        current_day += days_to_next_bribe
        current_savings += (days_to_next_bribe * salary) - bribe
        total_salary_earned += days_to_next_bribe * salary
        bribe += bribe_cost_increment
        salary += SALARY_INCREMENT

    return days_vs_earnings


def run_simulations():
    """
    Run simulations for several possible bribe increments
    """
    plot_type = LOGLOG
    days = 70
    inc_0 = greedy_boss(days, 0, plot_type)
    inc_500 = greedy_boss(days, 500, plot_type)
    inc_1000 = greedy_boss(days, 1000, plot_type)
    inc_2000 = greedy_boss(days, 2000, plot_type)
    simpleplot.plot_lines("Greedy boss", 600, 600, "days", "total earnings",
                          [inc_0, inc_500, inc_1000, inc_2000], False,
                          ["Bribe increment = 0", "Bribe increment = 500",
                           "Bribe increment = 1000", "Bribe increment = 2000"])


run_simulations()

print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]

print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
