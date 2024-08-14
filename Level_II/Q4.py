# Q4.py
def rotate_array(arr, d):
    n = len(arr)
    d = d % n
    return arr[-d:] + arr[:-d]

# Example usage
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    d = 2
    print("Array after rotation:", rotate_array(arr, d))
