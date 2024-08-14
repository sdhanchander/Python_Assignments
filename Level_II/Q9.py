# Q9.py
def safe_list_operation(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range"

# Example usage
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    index = 10
    print(safe_list_operation(my_list, index))
