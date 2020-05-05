# calculate future values
#  Print an introduction
# Input the amount of the principal ( principal )
# Input the amount of annual percentage rate ( apr )
# repeat 10 times
# principal = principal * ( 1 + apr )
# output the value of principal

'''
 A program to compute the value of an investment
 carried 10 years into the future
 '''

def main():
     print("This program calculate the future value")
     print("of a 10-year investment.")
     principal = eval(input("Enter the initial principal: "))
     apr = eval(input("Enter the annual interest rate: "))

     for i in range(10):
           principal = principal * (1 + apr)

     print("The value in 10 years is:", principal)

main()