import json

from common.read_file import get_input_as_strings


class Operations():
    def __init__(self, operations):
        self.op_id = 0
        self.acc_total = 0
        self.operations_executed = 0
        self.is_running = False
        self.operations = operations
        self.repeated_operation = []

    def _get_operation(self):
        return self.operations[self.op_id]

    def _oper_nop(self, operation):
        self.operations[self.op_id].update({'called_count': operation['called_count'] + 1})
        self.op_id += 1

    def _oper_acc(self, operation):
        self.acc_total += operation['amount']
        self.operations[self.op_id].update({'called_count': operation['called_count'] + 1})
        self.op_id += 1

    def _oper_jmp(self, operation):
        self.operations[self.op_id].update({'called_count': operation['called_count'] + 1})
        self.op_id += operation['amount']

    def _execute_operation(self):
        operation = self._get_operation()
        # print(operation)
        if operation['called_count'] > 0:
            self.repeated_operation.append(self.op_id)
            self._halt()
        elif len(self.operations) <= self.op_id:
            self._halt()
        elif operation['operation'] == 'nop':
            self._oper_nop(operation)
        elif operation['operation'] == 'acc':
            self._oper_acc(operation)
        elif operation['operation'] == 'jmp':
            self._oper_jmp(operation)
        else:
            self._halt()
            print(f"Error: Unsupported action: {operation['operation']}")
        # print(f'new op_id: {self.op_id}')

    def _halt(self):
        self.is_running = False

    def execute(self):
        self.op_id = 0
        self.is_running = True
        while self.is_running:
            self._execute_operation()
            self.operations_executed += 1
        return self.acc_total


def part1():
    print(_find_beginning_of_loop("input/day_08"))
    # answer: 1134


def part2():
    print(_do_second_thing("input/day_08"))


def _find_beginning_of_loop(input_file):
    operations = _parse_input(input_file)
    count = operations.execute()
    return count


def _do_second_thing(input_file):
    input_content = _parse_input(input_file)
    return 0


def _parse_input(input_file):
    parsed_lines = []
    lines = get_input_as_strings(input_file)
    for line in lines:
        op, amount = line.split()
        dict_op = {'operation': op, 'amount': int(amount), 'called_count': 0}
        parsed_lines.append(dict_op)
    # print(json.dumps(parsed_lines, indent=4))
    operations = Operations(parsed_lines)
    return operations
