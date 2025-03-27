with open("dataset1.csv", "r") as dataset1:
    # Read the entire file
    content = dataset1.read() # read() gets the full file content in str format
    print(content)
    content_in_lines = content.split("\n")
    print(content_in_lines)


with open("dataset2.csv", "r") as dataset2:
    # Read the entire file
    content = dataset2.readlines()
    for line in content:
        print(line)