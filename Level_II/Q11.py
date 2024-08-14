# Q11.py
def create_list_of_chars(strings):
    return list(map(list, strings))

# Example usage
if __name__ == "__main__":
    input_list = ['Red', 'Blue', 'Black', 'White', 'Pink']
    print(create_list_of_chars(input_list))
