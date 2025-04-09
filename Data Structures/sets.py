#Implement a program that uses sets to find the unique words in a given text file

text = "Implement a program that uses sets to find the unique words in a given text file"
list_of_strings = text.split(' ')

# Convert to lowercase for case-insensitive comparison
unique_words = set(word.lower() for word in list_of_strings)

print(unique_words)