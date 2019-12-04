


def not_decrease(n):
    previous = -1
    for d in map(int, str(n)):
        if d < previous:
            return False
        previous = d
    return True


def group_size(n, index):
    digits = [int(i) for i in str(n)]
    k=index + 1
    size = 1
    while k < len(digits):
        if digits[k] == digits[k-1]:
            size = size + 1
        else:
            return size
        k = k + 1

    return size



def two_adjacent_same(n):
    previous = -1
    for d in map(int, str(n)):
        if d == previous:
            return True
        previous = d
    return False


def two_adj_same_bis(n):
    digits = [int(i) for i in str(n)]
    k = 0
    while k < len(digits):
        size = group_size(n, k)
        if size == 2:
            return True
        k = k+size
    return False


def meets_criteria(n):
    return not_decrease(n) and two_adj_same_bis(n)


start = 240298
end = 784956

found = 0


for k in range(start, end):
    if meets_criteria(k):
        found = found + 1

print found




