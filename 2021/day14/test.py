import numpy as np
import heapq
import statistics
import math
from copy import deepcopy
from pprint import pprint

# "BCFHKNOPSV"
# "CHNB"

def save_input():
    with open("input") as f:
        input_string = f.read()
    parts = input_string.strip().split("\n\n")
    polymer = list(parts[0])
    rules = {}
    rules_input = parts[1].splitlines()
    for rule in rules_input:
        rule_list = rule.split(" -> ")
        rules[rule_list[0]] = rule_list[1]

    return polymer, rules


def part2(polymer, rules):
    # count_times = {"C": 0, "H": 0, "N": 0, "B": 0}
    count_times = {"B": 0, "C": 0, "F": 0, "H": 0, "K": 0, "N": 0, "O": 0, "P": 0, "S": 0, "V": 0}
    count_rules = {}
    for rule in rules:
        count_rules[rule] = 0

    for j in range(len(polymer) - 1):
        letter = "".join((polymer[j], polymer[j+1]))
        count_rules[letter] += 1

    for i in range(40):
        tmp_count_rules = {}
        for rule in rules:
            tmp_count_rules[rule] = 0
        update_rules = []
        for rule in count_rules:
            if count_rules[rule] > 0:
                update_rules.append(rule)
        for update_rule in update_rules:
            tmp_count_rules["".join([update_rule[0], rules[update_rule]])] += count_rules[update_rule]
            tmp_count_rules["".join([rules[update_rule], update_rule[1]])] += count_rules[update_rule]

        count_rules = tmp_count_rules

    for rule in count_rules:
        count_times[rule[0]] += count_rules[rule]
        count_times[rule[1]] += count_rules[rule]
    for letter in count_times:
        count_times[letter] = math.ceil(count_times[letter] / 2)

    nums = []
    for key in count_times:
        nums.append(count_times[key])

    return max(nums) - min(nums)


def part3(polymer, rules, num_of_iterations):
    count_rules = {}
    for j in range(len(polymer) - 1):
        letter = "".join((polymer[j], polymer[j+1]))
        try:
            count_rules[letter] += 1
        except KeyError:
            count_rules[letter] = 1

    for i in range(num_of_iterations):
        tmp_count_rules = {}
        for update_rule in count_rules:
            first_part = "".join([update_rule[0], rules[update_rule]])
            second_part = "".join([rules[update_rule], update_rule[1]])
            try:
                tmp_count_rules[first_part] += count_rules[update_rule]
            except KeyError:
                tmp_count_rules[first_part] = count_rules[update_rule]
            try:
                tmp_count_rules[second_part] += count_rules[update_rule]
            except KeyError:
                tmp_count_rules[second_part] = count_rules[update_rule]
        count_rules = tmp_count_rules

    count_times = {}
    for rule in count_rules:
        try:
            count_times[rule[0]] += count_rules[rule]
        except KeyError:
            count_times[rule[0]] = count_rules[rule]
        try:
            count_times[rule[1]] += count_rules[rule]
        except KeyError:
            count_times[rule[1]] = count_rules[rule]
    for letter in count_times:
        count_times[letter] = math.ceil(count_times[letter] / 2)

    count_list = list(count_times.values())
    return max(count_list) - min(count_list)


def search_in_rules(first, second, rules):
    for rule in rules:
        pol = "".join([first, second])
        if pol == rule[0]:
            return rule[0], rule[1]


def add_to_polymer(add_res, polymer):
    new_pol = []
    for i in range(len(polymer)):
        new_pol.append(polymer[i])
        if i in add_res:
            new_pol.append(add_res[i])
    return new_pol


def count_polymer(polymer):
    count = {}
    for letter in polymer:
        if letter not in count:
            count[letter] = 1
        else:
            count[letter] += 1

    nums = []
    for key in count:
        nums.append(count[key])

    return max(nums) - min(nums)


def part1(polymer, rules):
    for i in range(10):
        add_res = {}
        for j in range(len(polymer) - 1):
            add_res[j] = search_in_rules(polymer[j], polymer[j+1], rules)
        polymer = add_to_polymer(add_res, polymer)

    return count_polymer(polymer)


def main():
    polymer, rules = save_input()
    print(part3(polymer, rules, 10))


if __name__ == "__main__":
    main()
