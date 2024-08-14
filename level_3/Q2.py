# Q2.py
def count_lines(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return len(lines)

# Example usage
if __name__ == "__main__":
    filename = 'demo.txt'
    print("Number of lines:", count_lines(filename))
