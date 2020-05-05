# try / except block

x = input("Please Enter Hours: ") 
y = input("Please Enter Rate: ")
try:
    x = int(x) 
    y = int(y)
    z = x * y
    if x > 0 and y > 0 : 
        print("Enter Hours: ",x)
        print("Enter Rate: ",y)
        print("Total wage: ",z)
except: 
        print("Error, please enter numeric input")