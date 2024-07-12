# This is a Python script to demonstrate file handling in Python

# Open a file for reading
f = open('data.txt', 'r')

# Read the entire contents of the file into a string
read_data = f.read()

# Close the file
f.close()

# Print the contents of the file
print(read_data)

# Open the file again for reading
f = open('data.txt', 'r')

# Read the lines of the file into a list
method1 = list(f)

# Close the file
f.close()

# Print the list of lines using method 1
print(method1)

# Open the file again for reading
f = open('data.txt', 'r')

# Read the lines of the file into a list
method2 = f.readlines()

# Close the file
f.close()

# Print the list of lines using method 2
print(method2)
