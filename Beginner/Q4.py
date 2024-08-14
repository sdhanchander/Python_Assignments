def sum_of_odd_numbers(start, stop):
    return sum(x for x in range(start, stop + 1) if x % 2 != 0)

