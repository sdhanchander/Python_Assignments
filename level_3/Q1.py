# Q1.py
def even_length_strings(filename):
    even_length_strings = []
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into words and check each word
            words = line.split()
            for word in words:
                if len(word) % 2 == 0:
                    even_length_strings.append(word)
    return even_length_strings

# Example usage
if __name__ == "__main__":
    filename = 'doc.txt'
    print("Even length strings:", even_length_strings(filename))
