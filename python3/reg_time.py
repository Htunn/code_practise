# Search for lines that start with from and a character
# followed by a two digit number between 00 and 99 followed by ':'
# then print the number if it is greater than zero

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('^From .* ([0-9][0-9]):', line)
    if len(x) > 0:
        print(x)
