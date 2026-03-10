# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.

# Use words.txt as the file name
fname = input("Enter file name: ")

try:

	fh = open(fname)

	for line in fh:
		#remove whitespaces
		line = line.rstrip()
		print(line.upper())


except:
	print("File cannot be opened", fname)