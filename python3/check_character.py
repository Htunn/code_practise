# Check times of character

string1 = input('Please enter Word: ')
string2 = []
for i in string1:
    if i not in string2:
        string2.append(i)
    else:
        print(i)
        break
