# Character Frequency Counting in Python

# Using a plain dictionary
def char_frequency_dict(s):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

#  Using dict.get()
def char_frequency_dict_get(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

#  Using collections.Counter
from collections import Counter
def char_frequency_counter(s):
    return dict(Counter(s))

# Using str.count() method
def char_frequency_count_method(s):
    freq = {}
    for char in set(s):
        freq[char] = s.count(char)
    return freq

# Example
text = "Watermelon"

print("Method 1:", char_frequency_dict(text))
print("Method 2:", char_frequency_dict_get(text))
print("Method 3:", char_frequency_counter(text))
print("Method 4:", char_frequency_count_method(text))
