# search for lines that start with 'F', followed by
# 2 characters, followed by 'm:'

import re
hand = open('mbox.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
