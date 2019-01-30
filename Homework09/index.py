"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

# Used to increase the timeout, if necessary
import codeskulptor
codeskulptor.set_timeout(20)


def gen_all_sequences(outcomes, length):

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
    
    hand_score = []
    for dice_value in hand:
        hand_score.append(hand.count(dice_value) * dice_value)
    return max(hand_score)


def expected_value(held_dice, num_die_sides, num_free_dice):
    
    possible_hands = []
    value = 0

    possible_rolls = (gen_all_sequences((range(1, (num_die_sides + 1))), num_free_dice))

    for roll in possible_rolls:
        possible_hands.append(held_dice + roll)

    for hand in possible_hands:
        value += (float(score(hand)) / len(possible_hands))
    return value


def gen_all_holds(hand):
    
    all_holds_set = set([()])
    for dice_value in hand:
        hold_set = all_holds_set.copy()
        for hold in hold_set:
            temp = list(hold)
            temp.append(dice_value)
            temp = sorted(temp)
            all_holds_set.add(tuple(temp))
    return all_holds_set


def strategy(hand, num_die_sides):
    
    all_holds = gen_all_holds(hand)
    max_value = 0.0
    best_hold = ()
    for held_dice in all_holds:
        num_free_dice = len(hand)-len(held_dice)
        value = expected_value(held_dice, num_die_sides, num_free_dice)
        if value > max_value:
            best_hold = held_dice
            max_value = value
    return (max_value, best_hold)


def run_example():
    
    num_die_sides = 6
    hand = (2, 4, 6, 6, 1)
#    gen_all_holds(hand)
    hand_score, hold = strategy(hand, num_die_sides)
    print ("Best strategy for hand", hand, "is to hold", hold,"with expected score", hand_score)

run_example()