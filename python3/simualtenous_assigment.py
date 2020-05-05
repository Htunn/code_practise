# simualtenous assigment work for only numeric literal
# multiple values 
# A simple program to average two exam scores
# Illustrates use of multiple input

def main():
    print("This program computes the average of two exam scores.")

    score1, score2 = eval(input("Enter two scores seperated by comma: "))
    average = (score1 + score2) / 2

    print("The average of the score is:", average)

main()