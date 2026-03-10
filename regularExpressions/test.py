# Search for lines that contain 'From'
import re
hand = open('test.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)