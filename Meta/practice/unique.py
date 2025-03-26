"""
Input

file1
"happy"
"world"


file2
"happy"
"unique"
"content"

file3
"happy"
"content"


Gather/create a list of unique words across the files.


output

["happy", "word", "unique", "content"]


"""

file1 = ["happy", "world"]
file2 = ["happy", "unique", "content"]
file3 = ["happy", "content"]

# combine and strip quotes
all_words = file1 + file2 + file3
cleaned_words = [word.strip('"') for word in all_words]

# use dict.fromkeys to preserve order annd remove duplicates
unique_words = list(dict.fromkeys(cleaned_words))

print(unique_words)