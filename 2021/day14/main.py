import math


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


def solution(polymer, rules, num_of_iterations):
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


def main():
    polymer, rules = save_input()
    print(solution(polymer, rules, 100))


if __name__ == "__main__":
    main()
