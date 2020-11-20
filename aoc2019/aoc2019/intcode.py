import logging
import pdb

from .param_mode import ParamMode

logger = logging.getLogger(__name__)
logging_fh = logging.FileHandler('intcode.log', mode='w')
logger.addHandler(logging_fh)
logger.setLevel(logging.DEBUG)


def _sanitize_opcode(val):
    return str(val).zfill(5)


class IntCode():
    def __init__(self):
        self._logger = logging.getLogger(__name__)
        self._logger.debug(f"IntCode initialized")
        self._is_running = False
        self._cur_index = 0
        self._relative_base = 0
        self._user_input = []
        self._data = {}
        self.result_history = []
        self.halt_code_reached = False

    @property
    def result(self):
        return self.result_history[-1]

    def _get_operation(self, opcode):
        self._logger.debug(f"_get_operation({opcode=})")
        op_map = {
            "01": self._addition,
            "02": self._multiplication,
            "03": self._input,
            "04": self._output,
            "05": self._jump_if_true,
            "06": self._jump_if_false,
            "07": self._less_than,
            "08": self._equals,
            "09": self._relative_base_offset,
            "99": self._halt
        }
        return op_map.get(opcode)

    def get_input(self, input_file):
        with open(input_file, 'r') as fh:
            line = fh.readline().strip('\n')
            self._data = {index: int(value) for index, value in enumerate(line.split(","))}

    def set_user_input(self, user_input):
        if user_input:
            self._user_input.extend(user_input)

    def diagnostic_program(self):
        self._logger.debug("begin diagnostic_program()")
        self._is_running = True

        while self._is_running:
            self._logger.debug(f"{self._cur_index=}")
            opstring = _sanitize_opcode(self._get_value_from_data(self._cur_index))
            opcode = opstring[-2:]
            self._logger.debug(f"{opstring=} {opcode=}")

            operation = self._get_operation(opcode)
            operation(opstring)
            self._logger.debug("")

        self._logger.debug("end diagnostic_program()")
        self._logger.debug(f"return: {self._data[0]=}")
        return self._data[0]

    def _get_value_from_data(self, param):
        if param < 0:
            raise Exception(f"ERROR: invalid index: {param}")
        return self._data.get(param, 0)

    def _get_value(self, param, mode, is_dest):
        self._logger.debug(f"_get_value called with {param=} {mode=} {is_dest=}")
        param = int(param)
        mode = int(mode)
        if mode == ParamMode.RELATIVE:
            self._logger.debug(f"RELATIVE used: {param=} + {self._relative_base=}")
            self._logger.debug(f"returning {self._get_value_from_data(param + self._relative_base)}")
            if is_dest:
                return param + self._relative_base
            return self._get_value_from_data(param + self._relative_base)
        if mode == ParamMode.IMMEDIATE:
            return param
        if mode == ParamMode.POSITION:
            if is_dest:
                return param
            return self._get_value_from_data(param)
        raise Exception(f"{mode=}")

    def _increment_index(self, value):
        self._cur_index += value

    def _get_parameters(self, opstring, num_of_params, dest):
        self._logger.debug(f"{self._cur_index=}")
        self._logger.debug(f"{opstring=} {num_of_params=} {dest=}")
        mode_string = opstring[:-2]
        parameters = []
        for i in range(num_of_params):
            self._logger.debug(f"{i=}")
            parameter_mode = mode_string[-1 - i]
            parameter = self._get_value_from_data(self._cur_index + i + 1)
            parameter_val = self._get_value(parameter, parameter_mode, i == dest)
            parameters.append(parameter_val)

        return tuple(parameters)

    def _sanitize_opstring(self, opstring, num_of_params):
        # TODO: Finish this method
        """
        Remove unneeded characters from opstring and reverse ordering. This allows of easy
        interation of them with parameters since they will both be incrementing.
        """
        sanitized_opstring = opstring
        return sanitized_opstring

    def _addition(self, opstring):
        """Opcode 1 adds together numbers read from two positions and stores the result in a
        third position. The three integers immediately after the opcode tell you these three
        positions - the first two indicate the positions from which you should read the
        input values, and the third indicates the position at which the output should be
        stored.
        For example, if your Intcode computer encounters 1,10,20,30, it should read the
        values at positions 10 and 20, add those values, and then overwrite the value at
        position 30 with their sum."""
        self._logger.debug(f"_addition({opstring=})")
        parameters = self._get_parameters(opstring, 3, 2)
        self._logger.debug(f"{parameters=}")
        self._data[parameters[2]] = parameters[0] + parameters[1]
        self._logger.debug(f"{self._data[parameters[2]]=}")
        self._increment_index(4)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _multiplication(self, opstring):
        """Opcode 2 works exactly like opcode 1, except it multiplies the two inputs instead
        of adding them. Again, the three integers after the opcode indicate where the inputs
        and outputs are, not their values."""
        self._logger.debug(f"_multiplication({opstring=})")
        parameters = self._get_parameters(opstring, 3, 2)
        self._logger.debug(f"{parameters=}")
        self._data[parameters[2]] = parameters[0] * parameters[1]
        self._logger.debug(f"{self._data[parameters[2]]=}")
        self._increment_index(4)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _input(self, opstring):
        """Opcode 3 takes a single integer as input and saves it to the
           position given by its only parameter.
           For example, the instruction 3,50 would take an input value and store it at
           address 50."""
        self._logger.debug(f"_input({opstring=})")
        if len(self._user_input) == 0:
            self._is_running = False
            return
        parameters = self._get_parameters(opstring, 1, 0)
        self._logger.debug(f"{parameters=}")
        self._data[parameters[0]] = self._user_input.pop(0)
        self._logger.debug(f"{self._data[parameters[0]]=}")
        self._increment_index(2)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _output(self, opstring):
        """Opcode 4 outputs the value of its only parameter.
        For example, the instruction 4,50 would output the value at address 50."""
        self._logger.debug(f"_output({opstring=})")
        parameters = self._get_parameters(opstring, 1, None)
        self._logger.debug(f"{parameters=}")
        self.result_history.append(parameters[0])
        self._logger.debug(f"result_history.append({parameters[0]=})")
        self._increment_index(2)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _jump_if_true(self, opstring):
        """Opcode 5 is jump-if-true: if the first parameter is non-zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise, it does
        nothing."""
        self._logger.debug(f"_jump_if_true({opstring=})")
        parameters = self._get_parameters(opstring, 2, None)
        self._logger.debug(f"{parameters=}")
        if parameters[0] != 0:
            self._cur_index = parameters[1]
            self._logger.debug(f"next index= {self._cur_index=}")
        else:
            self._increment_index(3)
            self._logger.debug("JT incrementing index by 3")
            self._logger.debug(f"next index= {self._cur_index=}")

    def _jump_if_false(self, opstring):
        """Opcode 6 is jump-if-false: if the first parameter is zero, it sets the
        instruction pointer to the value from the second parameter. Otherwise, it does
        nothing."""
        self._logger.debug(f"_jump_if_false({opstring=})")
        parameters = self._get_parameters(opstring, 2, None)
        self._logger.debug(f"{parameters=}")
        if parameters[0] == 0:
            self._cur_index = parameters[1]
            self._logger.debug(f"next index= {self._cur_index=}")
        else:
            self._increment_index(3)
            self._logger.debug("JF incrementing index by 3")
            self._logger.debug(f"next index= {self._cur_index=}")

    def _less_than(self, opstring):
        """Opcode 7 is less than: if the first parameter is less than the second parameter,
        it stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        self._logger.debug(f"_less_than({opstring=})")
        parameters = self._get_parameters(opstring, 3, 2)
        self._logger.debug(f"{parameters=}")
        if parameters[0] < parameters[1]:
            self._data[parameters[2]] = 1
        else:
            self._data[parameters[2]] = 0
        self._logger.debug(f"{self._data[parameters[2]]=}")
        self._increment_index(4)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _equals(self, opstring):
        """Opcode 8 is equals: if the first parameter is equal to the second parameter, it
        stores 1 in the position given by the third parameter. Otherwise, it stores 0."""
        self._logger.debug(f"_equals({opstring=})")
        parameters = self._get_parameters(opstring, 3, 2)
        self._logger.debug(f"{parameters=}")
        if parameters[0] == parameters[1]:
            self._data[parameters[2]] = 1
        else:
            self._data[parameters[2]] = 0
        self._logger.debug(f"{self._data[parameters[2]]=}")
        self._increment_index(4)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _relative_base_offset(self, opstring):
        self._logger.debug(f"_relative_base_offset({opstring=})")
        self._logger.debug("_relative_base_offset called")
        self._logger.debug(f"offset: {self._relative_base=}")
        parameters = self._get_parameters(opstring, 1, None)
        self._relative_base += parameters[0]
        self._logger.debug(f"offset: {self._relative_base=}")
        self._increment_index(2)
        self._logger.debug(f"next index= {self._cur_index=}")

    def _halt(self, _=None):
        self._logger.debug("_halt() called")
        self._is_running = False
        self.halt_code_reached = True
