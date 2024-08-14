def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

# Example usage
print(are_anagrams("listen", "silent"))
