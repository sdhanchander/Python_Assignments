# Q8.py
def decode_string(encoded_string):
    parts = encoded_string.split('0')
    return {
        'first_name': parts[0],
        'last_name': parts[1],
        'id': parts[2]
    }

# Example usage
if __name__ == "__main__":
    encoded_string = "Robert000Smith000123"
    decoded_dict = decode_string(encoded_string)
    print("Decoded dictionary:", decoded_dict)
