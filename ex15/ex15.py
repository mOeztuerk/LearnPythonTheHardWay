# import modules
from sys import argv
# commandline parameters
script, filename = argv
"""
# txt is a choosen file from commandline
txt = open(filename)
# print the content of this file
print("Here is your file {}:".format(filename))
print(txt.read())
txt.close()

"""
# retype the name of the file
print("Type the filename again:")
file_again = input("> ")
# open file to a variable
txt_again = open(file_again)
# print content
print(txt_again.read())
txt_again.close()
