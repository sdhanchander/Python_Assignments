# Q8.py
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

# Example usage
if __name__ == "__main__":
    string = "Hello, World!"
    print(f"Number of vowels: {count_vowels(string)}")
