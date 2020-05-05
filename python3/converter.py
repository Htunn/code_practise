'''
Input the temperature in degree Celsius( call celsius )
convert the fahrenheit as (9/5)celsius + 32
output fahrenheit
'''

# convert.py
# A program to convert celsius to fahrenheit
# by htunnthuthuu

def main():
    celsius = eval(input("What is the Celsius Temperature? "))
    fahrenheit = 9//5 * celsius + 32
    print("The temperature is", fahrenheit, "degree Fahrenheit.")

main()