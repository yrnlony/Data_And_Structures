# Function to insert a string at a given position with proper spacing
def insert_string(original, to_insert, position):
    if position < 0 or position > len(original):
        raise ValueError("Position out of bounds")

    # Remove extra spaces at the insertion point edges
    before = original[:position].rstrip()  # remove trailing spaces before position
    after = original[position:].lstrip()  # remove leading spaces after position

    # Combine with a single space between
    return before + " " + to_insert.strip() + " " + after


# Example usage
original_string = "Arise, Its a new day!"
string_to_insert = "Much awaits"
position = 7

# Insert and print result
result = insert_string(original_string, string_to_insert, position)
print(result)  # Output:Arise, Much awaits It's a new day!
