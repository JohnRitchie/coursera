"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import SimpleGUICS2Pygame.codeskulptor as codeskulptor

codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score
    """
    result = 0

    for dummy_dice in hand:
        tmp_score = hand.count(dummy_dice) * dummy_dice

        if tmp_score > result:
            result = tmp_score

    return result


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    # if len(held_dice) + num_free_dice != 5:
    #     raise StandardError

    all_sides = list(range(1, num_die_sides + 1))
    all_rolls = gen_all_sequences(all_sides, num_free_dice)
    exp = 0

    for roll in all_rolls:
        exp += score(tuple(list(roll) + list(held_dice)))

    exp = float(exp) / len(all_rolls)
    return exp


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])

    if len(hand) == 0:
        return answer_set
    else:
        temp_hands = hand[:-1]
        for dummy_each_tuple in gen_all_holds(temp_hands):
            answer_set.add(dummy_each_tuple)
            answer_set.add((dummy_each_tuple + (hand[-1],)))

    return answer_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    score = 0.0
    hold = ()

    for dummy_hold in gen_all_holds(hand):
        tmp_score = expected_value(dummy_hold, num_die_sides, len(hand) - len(dummy_hold))
        if tmp_score > score:
            score = tmp_score
            hold = dummy_hold

    return score, hold


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


if __name__ == "__main__":
    run_example()
