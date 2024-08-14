def lcm(x, y):
    from math import gcd
    return x * y // gcd(x, y)

# Example usage
print("LCM of 12 and 18 is:", lcm(12, 18))
