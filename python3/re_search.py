# import regular expression library

import re
hand = open(input('Enter file name: '))
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
