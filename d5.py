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


def calculator(input_nb):
    data = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1002, 114, 46, 224, 1001, 224, -736, 224, 4, 224, 1002,
            223, 8, 223, 1001, 224, 3, 224, 1, 223, 224, 223, 1, 166, 195, 224, 1001, 224, -137, 224, 4, 224, 102, 8,
            223, 223, 101, 5, 224, 224, 1, 223, 224, 223, 1001, 169, 83, 224, 1001, 224, -90, 224, 4, 224, 102, 8, 223,
            223, 1001, 224, 2, 224, 1, 224, 223, 223, 101, 44, 117, 224, 101, -131, 224, 224, 4, 224, 1002, 223, 8,
            223, 101, 5, 224, 224, 1, 224, 223, 223, 1101, 80, 17, 225, 1101, 56, 51, 225, 1101, 78, 89, 225, 1102, 48,
            16, 225, 1101, 87, 78, 225, 1102, 34, 33, 224, 101, -1122, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 7,
            224, 224, 1, 223, 224, 223, 1101, 66, 53, 224, 101, -119, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5,
            224, 1, 223, 224, 223, 1102, 51, 49, 225, 1101, 7, 15, 225, 2, 110, 106, 224, 1001, 224, -4539, 224, 4,
            224, 102, 8, 223, 223, 101, 3, 224, 224, 1, 223, 224, 223, 1102, 88, 78, 225, 102, 78, 101, 224, 101,
            -6240, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 5, 224, 224, 1, 224, 223, 223, 4, 223, 99, 0, 0, 0, 677,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105, 0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0,
            256, 1105, 1, 99999, 1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105,
            1, 99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1, 99999, 1106,
            0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1, 99999, 1107, 226, 677, 224,
            102, 2, 223, 223, 1006, 224, 329, 101, 1, 223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 344,
            101, 1, 223, 223, 8, 226, 677, 224, 102, 2, 223, 223, 1006, 224, 359, 1001, 223, 1, 223, 1007, 226, 677,
            224, 1002, 223, 2, 223, 1005, 224, 374, 101, 1, 223, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1005,
            224, 389, 1001, 223, 1, 223, 1108, 677, 226, 224, 1002, 223, 2, 223, 1006, 224, 404, 1001, 223, 1, 223,
            1007, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 419, 1001, 223, 1, 223, 1107, 677, 226, 224, 1002, 223,
            2, 223, 1006, 224, 434, 101, 1, 223, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1005, 224, 449, 1001, 223,
            1, 223, 1107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 464, 1001, 223, 1, 223, 108, 226, 226, 224, 1002,
            223, 2, 223, 1006, 224, 479, 1001, 223, 1, 223, 1008, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 494, 101,
            1, 223, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 509, 1001, 223, 1, 223, 8, 677, 226, 224,
            1002, 223, 2, 223, 1006, 224, 524, 101, 1, 223, 223, 7, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 539,
            101, 1, 223, 223, 7, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 554, 1001, 223, 1, 223, 7, 226, 226, 224,
            1002, 223, 2, 223, 1006, 224, 569, 101, 1, 223, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 584,
            101, 1, 223, 223, 1108, 677, 677, 224, 102, 2, 223, 223, 1006, 224, 599, 1001, 223, 1, 223, 1008, 677, 226,
            224, 1002, 223, 2, 223, 1005, 224, 614, 1001, 223, 1, 223, 8, 677, 677, 224, 1002, 223, 2, 223, 1006, 224,
            629, 1001, 223, 1, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1006, 224, 644, 101, 1, 223, 223, 1007, 677,
            677, 224, 102, 2, 223, 223, 1006, 224, 659, 101, 1, 223, 223, 107, 226, 226, 224, 1002, 223, 2, 223, 1006,
            224, 674, 1001, 223, 1, 223, 4, 223, 99, 226]

    # data = [3,0,4,0,99]

    def get_param_value(param, mode):
        if mode == 0:
            return data[param]
        if mode == 1:
            return param

        print "Err: Unknown mode " + str(mode)

    def do_instruction(data, i):

        instr = decode_instruction(data[i])
        code = instr["code"]

        first = data[i + 1]

        if code == 99:
            print "End"
            exit(0)

        if code == 3:
            data[first] = input_nb
            return instr["len"] + i

        if code == 4:
            first_evaluated = first #get_param_value(first, instr["mode1"])
            out = data[first_evaluated]
            print "output: " + str(out)
            if out != 0:
                print "ERRR"
            return instr["len"] + i

        second = data[i + 2]
        pos = data[i + 3]

        first_evaluated = get_param_value(first, instr["mode1"])
        second_evaluated = get_param_value(second, instr["mode2"])
        #pos = get_param_value(pos, instr["mode3"])

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
            print "Err: Invalid code " + str(code)

        print "idx " + str(i) + " instr:" + str(instr) + "first [" + str(first) + "," + str(
              first_evaluated) + "] " + " second [" + str(second) + "," + str(second_evaluated) + "]" + " => data[" + str(pos) + "]=" + str(val)

        return instr["len"] + i

    idx = 0
    while idx < len(data):
        idx = do_instruction(data, idx)


calculator(5)
