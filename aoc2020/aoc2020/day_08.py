import json

from common.read_file import get_input_as_strings


class Operations():
    def __init__(self, operations):
        self.op_id = 0
        self.acc_total = 0
        self.operations_executed = 0
        self.is_running = False
        self.operations = operations.copy()
        self._unmodified_operations = operations.copy()
        self._nop_list = self._get_nop_list()
        self._jmp_list = self._get_jmp_list()
        self.repeated_operation = []
        self._infinite_loop_detected = False

    def get_operation(self, op_id):
        return self.operations[op_id]

    def set_operation(self, op_id, oper_dict):
        self.operations[op_id].update(oper_dict)

    def reset_operations(self):
        self.op_id = 0
        self.acc_total = 0
        self.reset_called_counts()
        self._infinite_loop_detected = False

    def reset_called_counts(self):
        for o in self.operations:
            o.update({'called_count': 0})

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
        if len(self.operations) <= self.op_id:
            # print('Operation terminated successfully')
            self._halt()
            return
        operation = self.get_operation(self.op_id)
        # print(f'{self.op_id=} {operation=}')
        if operation['called_count'] > 0:
            # print('Infinite loop detected')
            self._infinite_loop_detected = True
            self.repeated_operation.append(self.op_id)
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

    def _halt(self):
        self.is_running = False

    def execute(self):
        self.op_id = 0
        self.is_running = True
        while self.is_running:
            self._execute_operation()
            self.operations_executed += 1
        return self.acc_total

    def _get_nop_list(self):
        nop_list = []
        op_id = 0
        for operation in self._unmodified_operations:
            if operation['operation'] == 'nop':
                nop_dict = {'op_id': op_id, 'amount': operation['amount'], 'changed_to_jmp': False}
                nop_list.append(nop_dict)
            op_id += 1
        return nop_list

    def _get_jmp_list(self):
        jmp_list = []
        op_id = 0
        for operation in self._unmodified_operations:
            if operation['operation'] == 'jmp':
                jmp_dict = {'op_id': op_id, 'amount': operation['amount'], 'changed_to_nop': False}
                jmp_list.append(jmp_dict)
            op_id += 1
        return jmp_list

    def print_operations(self):
        for o in self.operations:
            print(o)


def part1():
    print(_find_beginning_of_loop("input/day_08"))
    # answer: 1134


def part2():
    print(_find_corrupted_operation("input/day_08"))


def _find_beginning_of_loop(input_file):
    operations = _parse_input(input_file)
    operations.execute()
    return operations.acc_total


def _find_corrupted_operation(input_file):
    # print('==== nop -> jmp ====')
    operations = _parse_input(input_file)
    # operations.print_operations()
    for nop_oper in operations._nop_list:
        # print(f'{nop_oper=}')
        oper_dict = {'operation': 'jmp'}
        operations.set_operation(nop_oper['op_id'], oper_dict)
        operations.execute()
        if not operations._infinite_loop_detected:
            return operations.acc_total
        original_oper_dict = {'operation': 'nop'}
        operations.set_operation(nop_oper['op_id'], original_oper_dict)
        operations.reset_operations()
    # print('==== jmp -> nop ====')
    operations.reset_operations()
    for jmp_oper in operations._jmp_list:
        # print(f'{jmp_oper=}')
        oper_dict = {'operation': 'nop'}
        # operations.print_operations()
        operations.set_operation(jmp_oper['op_id'], oper_dict)
        # print("changed")
        # operations.print_operations()
        operations.execute()
        if not operations._infinite_loop_detected:
            return operations.acc_total
        # print("changed back")
        original_oper_dict = {'operation': 'jmp'}
        operations.set_operation(jmp_oper['op_id'], original_oper_dict)
        # print()
        operations.reset_operations()
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
