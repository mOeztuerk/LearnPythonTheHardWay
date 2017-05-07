from sys import argv
from os.path import exists

script, from_file, to_file = argv

print("Copying from  {} to {}".format(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print("Does the output file exist? {}".format(exists(to_file)))

out_file = open(to_file, "w")
out_file.write(indata)

print("Done")

out_file.close()
in_file.close()
