# Q9.py
def run_length_encoding(input_string):
    encoded_string = []
    i = 0
    while i < len(input_string):
        count = 1
        while i + 1 < len(input_string) and input_string[i] == input_string[i + 1]:
            i += 1
            count += 1
        encoded_string.append(f"{input_string[i]}{count}")
        i += 1
    return ''.join(encoded_string)

# Example usage
if __name__ == "__main__":
    input_string = "wwwwaaadebbbbbw"
    encoded_string = run_length_encoding(input_string)
    print("Run length encoded string:", encoded_string)
