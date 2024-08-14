def is_perfect_number(num):
    if num < 1:
        return "No"
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    return "Yes" if divisors_sum == num else "No"


