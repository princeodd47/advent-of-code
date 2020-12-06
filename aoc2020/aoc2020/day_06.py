from common.read_file import get_input_as_strings


def part1():
    print(anyone_answered_yes("input/day_06"))
    # answer: 6249


def part2():
    print(everyone_answered_yes("input/day_06"))
    # answer: 3103


def anyone_answered_yes(input_file):
    group_answers = []
    lines = get_input_as_strings(input_file)
    answers = ''
    for line in lines:
        if line != '':
            if answers == '':
                answers = line
            else:
                answers += line
        else:
            group_answers.append(set(answers))
            answers = ''

    group_answers.append(set(answers))
    count = 0
    for a in group_answers:
        count += len(a)
    return count


def everyone_answered_yes(input_file):
    group_answers = []
    lines = get_input_as_strings(input_file)
    answers = []
    for line in lines:
        if line != '':
            answers.append(set(line))
        else:
            group_answers.append(set.intersection(*answers))
            answers.clear()

    group_answers.append(set.intersection(*answers))
    count = 0
    for a in group_answers:
        count += len(a)
    return count
