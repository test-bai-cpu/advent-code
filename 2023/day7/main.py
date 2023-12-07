from pprint import pprint
import sys
from collections import Counter

def save_input():
    with open("input") as f:
    # with open("sampleinput") as f:
        input_str = f.read()
    data = input_str.strip().splitlines()
    return data

def get_hand_type(hand):
    card_counts = Counter(list(hand))

    if len(card_counts) == 1 and 5 in card_counts.values():
        return "five_kind"
    elif 4 in card_counts.values():
        return "four_kind"
    elif len(card_counts) == 2 and set(card_counts.values()) == {2, 3}:
        return "full_house"
    elif set(card_counts.values()) == {1, 3} and len(card_counts) == 3:
        return "three_kind"
    elif list(card_counts.values()).count(2) == 2 and len(card_counts) == 3:
        return "two_pair"
    elif 2 in card_counts.values() and len(card_counts) == 4:
        return "one_pair"
    else:
        return "high_card"
    
def get_hand_type_with_J(hand):
    card_counts = Counter(list(hand))
    # print(card_counts)
    if len(card_counts) == 1 and 5 in card_counts.values():
        return "five_kind"
    elif 4 in card_counts.values():
        if "J" in list(hand):
            return "five_kind"
        return "four_kind"
    elif len(card_counts) == 2 and set(card_counts.values()) == {2, 3}:
        if "J" in list(hand):
            return "five_kind"
        return "full_house"
    elif set(card_counts.values()) == {1, 3} and len(card_counts) == 3:
        if "J" in list(hand):
            return "four_kind"
        return "three_kind"
    elif list(card_counts.values()).count(2) == 2 and len(card_counts) == 3:
        keys_with_count_one = [card for card, count in card_counts.items() if count == 1]
        keys_with_count_two = [card for card, count in card_counts.items() if count == 2]
        if "J" in keys_with_count_two:
            return "four_kind"
        if "J" in keys_with_count_one:
            return "full_house"
        return "two_pair"
    elif 2 in card_counts.values() and len(card_counts) == 4:
        if "J" in list(hand):
            return "three_kind"
        return "one_pair"
    else:
        if "J" in list(hand):
            return "one_pair"
        return "high_card"

def sort_hands(hands, card_order):
    rank_priority = {rank: i for i, rank in enumerate(card_order)}

    def hand_key(hand_tuple):
        hand = hand_tuple[0]
        return tuple(rank_priority[card] for card in hand)

    return sorted(hands, key=hand_key)

def part1(data):
    hands_all = {
        "five_kind": [],
        "four_kind": [],
        "full_house": [],
        "three_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": [],
    }
    
    card_order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    
    for row in data:
        hand, bid = row.split()
        hand_type = get_hand_type(hand)
        hands_all[hand_type].append((hand, bid))
    
    for hand_type in hands_all:
        hands_all[hand_type] = sort_hands(hands_all[hand_type], card_order)

    total_hands = []
    for hand_type in hands_all:
        total_hands += hands_all[hand_type]
    
    total_num = len(total_hands)
    sum = 0
    for i, hand in enumerate(total_hands):
        sum += (total_num - i) * int(hand[1])
    
    return sum
    
def part2(data):
    hands_all = {
        "five_kind": [],
        "four_kind": [],
        "full_house": [],
        "three_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": [],
    }
    
    card_order = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
    
    for row in data:
        hand, bid = row.split()
        hand_type = get_hand_type_with_J(hand)
        hands_all[hand_type].append((hand, bid))
    
    for hand_type in hands_all:
        hands_all[hand_type] = sort_hands(hands_all[hand_type], card_order)

    total_hands = []
    for hand_type in hands_all:
        total_hands += hands_all[hand_type]
    
    total_num = len(total_hands)
    sum = 0
    for i, hand in enumerate(total_hands):
        sum += (total_num - i) * int(hand[1])
    
    return sum

input_data = save_input()
print("part1: ", part1(input_data))
print("part2: ", part2(input_data))