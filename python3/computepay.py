# define compute function

hours = int(input("Enter Hour: "))
rate = int(input("Enter Rate: "))

def computepay(hours, rate):
    if hours > 40:
        pay = hours * rate
        return pay

x = computepay(hours, rate)
print("Pay: ",x)