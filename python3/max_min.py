# find the largest value in in a list

largest = None
print("Before: ", largest)
for itevar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itevar > largest:
        largest = itevar
    print('Loop:', itevar, largest)
print('Largest: ', largest)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print('Loop:', itervar, smallest)
print("Smallest: ", smallest)
