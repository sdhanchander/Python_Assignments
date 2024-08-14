# Q13.py
def starts_with(input_string, given_char):
    return (lambda s, c: s.startswith(c))(input_string, given_char)

# Example usage
if __name__ == "__main__":
    input_string = "Hello, World!"
    given_char = "H"
    print(starts_with(input_string, given_char))
