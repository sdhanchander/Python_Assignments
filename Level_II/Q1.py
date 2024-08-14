# Q1.py
def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# Example usage
if __name__ == "__main__":
    l1 = [1, 2, 3, 4, 5]
    l2 = [4, 5, 6, 7, 8]
    print("Common elements:", common_elements(l1, l2))
