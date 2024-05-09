# Import the Counter class from collections module
from collections import Counter

# Define the file name
file_name = "text.txt"

# Create an empty list to store the words
words = []

# Open the file in read mode
with open(file_name, "r") as f:
  # Loop through each line in the file
  for line in f:
    # Split the line into words and append them to the list
    words.extend(line.lower().split())

# Create a Counter object from the list of words
word_counts = Counter(words)

# Get the most common words and their frequencies
most_common = word_counts.most_common()

# Print the results
print("The most frequent words in the file are:")
for word, count in most_common:
  print(f"{word}: {count} times")
