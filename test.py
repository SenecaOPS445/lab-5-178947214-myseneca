# Open the file 'data.txt' for reading ('r' 
f=open('data.txt', 'r')
# Read the entire content of the file into a variable
read_data = f.read()

# Close the file after reading
f.close()

# Print the content read from the file
print(read_data)


f = open('data.txt', 'r')
method1 = list(f)
f.close()
print(method1)
