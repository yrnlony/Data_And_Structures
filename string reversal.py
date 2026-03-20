# Method 1: Using slicing
text = "May the best team win"
reverse_slicing = text[::-1]
print(reverse_slicing)

# Method 2: Using a loop
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

reverse_loop = reverse_string(text)
print(reverse_loop)

# Method 3: Using reversed() + join()
def reverse_builtin(s):
    return ''.join(reversed(s))

reverse_builtin_result = reverse_builtin(text)
print(reverse_builtin_result)

# Using recursion
def reverse_recursive(s):
    if len(s) <= 1:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

reverse_recursive_result = reverse_recursive(text)
print(reverse_recursive_result)
