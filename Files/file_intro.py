# In Python, files are opened using the open function:
# The name of the file to open
filename = "starwars.txt"

# The mode in which to open it (read, text)
mode = "rt"

# Actually open the file
openfile = open(filename, mode)

# Open file objects have many different read methods, but the most basic is intuitively called read:
openfile = open("gonewiththewind.txt", "rt")

filedata = openfile.read()
print(filedata)

#Similarly, open file objects have many different write methods, but the most basic is intuitively called write:
openfile = open("mymoviescript.txt", "wt")

openfile.write('I wish I had an idea for a movie...\n')

#Finally, never forget to close the file! To do so, open file objects have a close method:
openfile = open("emptyfile.txt")

openfile.close()