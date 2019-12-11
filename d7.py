def decode_instruction(code):
    digits = [int(d) for d in str(code)]

    while len(digits) < 5:
        digits = [0] + digits

    code = digits[3] * 10 + digits[4]
    l = 4

    if code == 3 or code == 4:
        l = 2

    if code == 5 or code == 6:
        l = 3

    if code == 7 or code == 8:
        l = 4

    return {
        "code": code,
        "len": l,
        "mode1": digits[2],
        "mode2": digits[1],
        "mode3": digits[0]
    }


def extend(data, pos):
    if pos >= len(data):
        data = data + [0 for i in range(pos - len(data) + 1)]

    return data


class Calculator:
    def __init__(self, data):
        self.data = data
        self.input_queue = []
        self.input_queue.reverse()
        self.finished = False
        self.instruction_idx = 0

    def get_param_value(self, param, mode):
        if mode == 0:
            return self.data[param]
        if mode == 1:
            return param

        print("Err: Unknown mode " + str(mode))
        raise

    def do_instruction(self):
        instr = decode_instruction(self.data[self.instruction_idx])
        code = instr["code"]

        first = self.data[self.instruction_idx + 1]

        if code == 99:
            self.finished = True
            self.instruction_idx = len(self.data)
            return

        if code == 3:
            self.data[first] = self.input_queue.pop()
            self.instruction_idx = instr["len"] + self.instruction_idx
            return

        if code == 4:
            first_evaluated = first
            out = self.data[first_evaluated]
            self.instruction_idx = instr["len"] + self.instruction_idx
            print("output: " + str(out))
            return out

        second = self.data[self.instruction_idx + 2]
        pos = self.data[self.instruction_idx + 3]

        first_evaluated = self.get_param_value(first, instr["mode1"])
        second_evaluated = self.get_param_value(second, instr["mode2"])

        if code == 5:
            if first_evaluated != 0:
                self.instruction_idx = second_evaluated
            else:
                self.instruction_idx = instr["len"] + self.instruction_idx
            return

        if code == 6:
            if first_evaluated == 0:
                self.instruction_idx = second_evaluated
            else:
                self.instruction_idx = instr["len"] + self.instruction_idx
            return

        if code == 7:
            if first_evaluated < second_evaluated:
                self.data[pos] = 1
            else:
                self.data[pos] = 0
            self.instruction_idx = instr["len"] + self.instruction_idx
            return

        if code == 8:
            if first_evaluated == second_evaluated:
                self.data[pos] = 1
            else:
                self.data[pos] = 0
            self.instruction_idx = instr["len"] + self.instruction_idx
            return

        self.data = extend(self.data, pos)
        val = -1000
        if code == 1:
            val = first_evaluated + second_evaluated
            self.data[pos] = val
        elif code == 2:
            val = first_evaluated * second_evaluated
            self.data[pos] = val
        else:
            print("Err: Invalid code " + str(code))

        self.instruction_idx = instr["len"] + self.instruction_idx
        return

    def input(self, input):
        self.input_queue.insert(0, input)

    def run(self):
        output = None
        while output == None and self.finished == False:
            output = self.do_instruction()
        return output


def amplifiers(phase):
    data = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

    a = Calculator(data)
    a.input(phase[0])

    b = Calculator(data)
    b.input(phase[1])

    c = Calculator(data)
    c.input(phase[2])

    d = Calculator(data)
    d.input(phase[3])

    e = Calculator(data)
    e.input(phase[4])

    signal = 0

    while not (a.finished and b.finished and c.finished and d.finished and e.finished):
        a.input(signal)
        signal = a.run()

        b.input(signal)
        signal = b.run()

        c.input(signal)
        signal = c.run()

        d.input(signal)
        signal = d.run()

        e.input(signal)
        signal = e.run()

    return signal

result = amplifiers([9,8,7,6,5])

print(result)