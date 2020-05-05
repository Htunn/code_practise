# define computegrade function

w = float(input("Enter score: "))

def computegrade(w):
    if w >= 0.9:
        print("A")
    elif w >= 0.8:
        print("B")
    elif w >= 0.7:
        print("C")
    elif w >= 0.6:
        print("D")
    elif w < 0.6:
        print("F")
computegrade(w)