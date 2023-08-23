def longest_substring(s, k):
    if len(s) == 0:
        return 0
    
    # Count the frequency of each character in the string
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find the first character that appears less than k times
    for char in char_count:
        if char_count[char] < k:
            return max(longest_substring(subs, k) for subs in s.split(char))
    
    # If all characters appear at least k times, the whole string is valid
    return len(s)

# Example usage
s = "aaabb"
k = 3
print(longest_substring(s, k))  # Output: 3
