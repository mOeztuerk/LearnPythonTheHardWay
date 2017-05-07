from sys import argv

script, filename = argv

print("we are going to erase {}.".format(filename))
print("If you do not want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("opening the file..")
target = open(filename, "w")

print("Truncating the file. Cucu")
target.truncate()

print("now i am going to ask you for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I am going to write these to the file.")

target.write("{}\n{}\n{}\n".format(line1, line2, line3))

print("And finally we close it.")
target.close()
