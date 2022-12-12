# Define a list of strings
words = ['hello', 'world', 'foo', 'bar', 'baz']

# Define a function that returns True if a string is longer than 3 characters
def is_long(word):
  return len(word) > 3

# Use the filter() function to filter the list of strings
long_words = filter(is_long, words)

# Print the filtered list
print(list(long_words))

# made by KingTreemox aka Treemox