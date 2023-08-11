# key fx for working with files is open().
# 4 Diff methods/modes for file opening.
# r - opens file for reading, error if it doesn't exist.
# a - opens a file to append, creates new if it doesn't exist.
# w - opens a file for writing, creates the file if it doesn't exist.
# x - creates file, returns error if it exists.
# t for text mode.
# b for binary mode (images).

f = open("demo.txt")  # same as f = open("demo.txt", "rt") since rt are default, don't need to specify
# if in diff location...need to specify location--f = open("D:\\myfiles\welcome.txt", "r")
f.close()
f = open("demo.txt", "r")  # r means read
# print(f.read(3))  # opens and read only first 3 characters
print(f.readline())  # remove the print above, will return the first line if you call readline twice, you get 2 lines

f.close()  # closes file when finished.

# write to an existing file
a = open("demo2.txt", "a")  # running this without a created doc will create one, appends og file
a.write("\nThis was added using python code.")
a.close()

b = open("demo2.txt", "r")
print(b.read())

c = open("demo3.txt", "w")
c.write("This txt file was created USING python")
c.close()
d = open("demo3.txt", "r")
print(d.read())
d.close()

# deleting files
import os
os.remove("delete.txt")

if os.path.exists("delete2.txt"):
    os.remove("delete2.txt")
else:
    print("The file does not exist")

# os.rmdir("foldername") # use this to remove an empty folder
