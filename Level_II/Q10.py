# Q10.py
def calculate_stones(n):
    stones = []
    next_stone = 2
    while n > 0:
        if n >= next_stone:
            stones.append(next_stone)
            n -= next_stone
            next_stone += 2
        else:
            break
    return stones

# Example usage
if __name__ == "__main__":
    n = 7
    print(f"Stones in a single pile: {calculate_stones(n)}")
