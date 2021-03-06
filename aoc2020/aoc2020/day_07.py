import re

from common.read_file import get_input_as_strings


class Bag:
    def __init__(self, name, contents):
        self.name = name
        self.contents = contents


class Rules:
    def __init__(self, rules):
        self.rules = rules
        self.parent_bags = []
        self.total_bag_count = 0

    def get_parent_bags(self, desired_bag):
        for r in self.rules:
            if desired_bag in r.contents:
                # print(r.name, r.contents)
                self.parent_bags.append(r)
                self.get_parent_bags(r.name)

    def get_rule_by_name(self, desired_bag):
        return next((x for x in self.rules if x.name == desired_bag), None)

    def get_total_bag_count(self, desired_bag):
        count = 0
        bag = self.get_rule_by_name(desired_bag)
        if bag.contents:
            for bag_name, multiplier in bag.contents.items():
                count += multiplier * (1 + self.get_total_bag_count(bag_name))
            return count
        else:
            return 0


def part1():
    desired_bag = 'shiny gold'
    print(_get_max_parent_bag_count("input/day_07", desired_bag))


def part2():
    desired_bag = 'shiny gold'
    print(_get_total_bag_count("input/day_07", desired_bag))


def _get_max_parent_bag_count(input_file, desired_bag):
    rules = Rules(_parse_input(input_file))
    rules.get_parent_bags(desired_bag)
    return len(set(rules.parent_bags))


def _get_total_bag_count(input_file, desired_bag):
    rules = Rules(_parse_input(input_file))
    rules.get_parent_bags(desired_bag)
    return rules.get_total_bag_count(desired_bag)


def _parse_input(input_file):
    rules = []
    lines = get_input_as_strings(input_file)
    for line in lines:
        split_string = line.split(' bags contain ')
        bag_name = split_string[0]
        contents = _parse_contents(split_string[1])
        bag = Bag(bag_name, contents)
        rules.append(bag)
    return rules


def _parse_contents(string):
    string = string.replace('bags', 'bag')
    string = string.replace(' bag, ', ',')
    string = string.replace(' bag.', '')
    if string == "no other":
        return {}
    split_string = string.split(',')
    contents = {}
    for s in split_string:
        s_split = s.split()
        count = s_split[0]
        bag = re.sub(r'[0-9] ', '', s)
        contents[bag] = int(count)
    return contents
