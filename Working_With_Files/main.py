# Overwrite
with open('./my_file.txt', mode='w') as file:
    file.write('Before')
# Read
with open("./my_file.txt", mode='r') as file:
    contents = file.read()
    print(contents)
# Append
with open("./my_file.txt", mode='a') as file:
    file.write('\nAfter')
# Create a new File
with open('./New_file.txt', mode='w') as file:
    file.write('New')
# Getting a File from somewhere else using the '/' Root & working Directory
with open("/Users/USER/OneDrive/Desktop/New Text Document.txt", mode='r') as file:
    contents = file.read()
    print(contents)
# Getting a File from somewhere else with absolute directory
with open("../../Desktop/New Text Document.txt", mode='r') as file:
    contents = file.read()
    print(contents)

    # Absolute  File Paths are always relative to the root folder C:\

    # Relative File Paths are always relative to where you are currently working. 