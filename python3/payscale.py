# pay scale

x = int(input("Enter Hour: "))
y = 10 # pay compute rate for normal 
z = 1.5 # pay computation rate

if x > 40 :
    hour = int(x - 40)
    rate = y * z
    pay = (x * y) + (hour * rate) 
    print(pay)
else:
    pay = x * y 
    print(pay)