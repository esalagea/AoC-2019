from itertools import permutations


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


def calculator(queue, data):
    queue.reverse()
    output = -1
    halt = False

    # data = [3,0,4,0,99]

    def get_param_value(param, mode):
        if mode == 0:
            return data[param]
        if mode == 1:
            return param

        print("Err: Unknown mode " + str(mode))

    def do_instruction(data, i):
        nonlocal output
        nonlocal halt
        instr = decode_instruction(data[i])
        code = instr["code"]

        first = data[i + 1]

        if code == 99:
            halt = True
            exit(0)
            return len(data)

        if code == 3:
            data[first] = queue.pop()
            return instr["len"] + i

        if code == 4:
            first_evaluated = first
            out = data[first_evaluated]
            print("output: " + str(out))
            output = out

            return len(data)

        second = data[i + 2]
        pos = data[i + 3]

        first_evaluated = get_param_value(first, instr["mode1"])
        second_evaluated = get_param_value(second, instr["mode2"])

        if code == 5:
            if first_evaluated != 0:
                return second_evaluated
            else:
                return instr["len"] + i

        if code == 6:
            if first_evaluated == 0:
                return second_evaluated
            else:
                return instr["len"] + i

        if code == 7:
            if first_evaluated < second_evaluated:
                data[pos] = 1
            else:
                data[pos] = 0
            return instr["len"] + i

        if code == 8:
            if first_evaluated == second_evaluated:
                data[pos] = 1
            else:
                data[pos] = 0
            return instr["len"] + i

        data = extend(data, pos)
        val = -1000
        if code == 1:
            val = first_evaluated + second_evaluated
            data[pos] = val
        elif code == 2:
            val = first_evaluated * second_evaluated
            data[pos] = val
        else:
            print("Err: Invalid code " + str(code))
        return instr["len"] + i

    idx = 0
    while idx < len(data):
        idx = do_instruction(data, idx)

    return output, halt


def amplifiers(phase):
    data = [3, 52, 1001, 52, -5, 52, 3, 53, 1, 52, 56, 54, 1007, 54, 5, 55, 1005, 55, 26, 1001, 54,
            -5, 54, 1105, 1, 12, 1, 53, 54, 53, 1008, 54, 0, 55, 1001, 55, 1, 55, 2, 53, 55, 53, 4,
            53, 1001, 56, -1, 56, 1005, 56, 6, 99, 0, 0, 0, 0, 10]

    data_a = list(data)
    data_b = list(data)
    data_c = list(data)
    data_d = list(data)
    data_e = list(data)
    e = 0
    he = False
    while not he:
        a, ha = calculator([phase[0], e], data_a)
        b, hb = calculator([phase[1], a], data_b)
        c, hc = calculator([phase[2], b], data_c)
        d, hd = calculator([phase[3], c], data_d)
        e, he = calculator([phase[4], d], data_e)
        print(e)


def get_max_signal():
    max_signal = -1
    phases = list(permutations(range(5, 10)))
    print(phases)
    # phases = [list(t) for t in phases]
    # print(phases)
    #
    # for phase in phases:
    #     signal = amplifiers(phase)
    #     if signal > max_signal:
    #         max_signal = signal
    return max_signal


# print(get_max_signal())

amplifiers([9,7,8,5,6])
