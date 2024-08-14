# Q6.py
def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0:
        return False
    return is_power_of_two(n // 2)

# Example usage
if __name__ == "__main__":
    number = 16
    print(f"Is {number} a power of two? {is_power_of_two(number)}")
