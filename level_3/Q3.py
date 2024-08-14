# Q3.py
def JtoI(filename):
    with open(filename, 'r') as file:
        content = file.read()
    corrected_content = content.replace('J', 'I')
    print(corrected_content)

# Example usage
if __name__ == "__main__":
    filename = 'words.txt'
    JtoI(filename)
