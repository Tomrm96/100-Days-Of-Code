# Overwrite
with open('Day_24/my_file.txt', mode='w') as file:
    file.write('Before')
# Read
with open("Day_24/my_file.txt", mode='r') as file:
    contents = file.read()
    print(contents)
# Append
with open("Day_24/my_file.txt", mode='a') as file:
    file.write('\nAfter')
# Create a new File
with open('Day_24/New_file.txt', mode='w') as file:
    file.write('New')