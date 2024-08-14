def count_digits_and_letters(s):
    digits = sum(c.isdigit() for c in s)
    letters = sum(c.isalpha() for c in s)
    return f"Alphabets: {letters} & Number : {digits}"

# Example usage
print(count_digits_and_letters("Hello123"))
