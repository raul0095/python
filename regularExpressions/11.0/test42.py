# Search for lines that contain 'From'
import re
hand = open('regex_sum_42.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for num in numbers:
        numlist.append(int(num))
print("Total:", sum(numlist))
# output Total: 445833



