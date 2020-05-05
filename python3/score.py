# score.py

w = input("Enter Score: ")
try:
    w = float(w)
    if w >= 0.9 :
        print("A")
    elif w >= 0.8 :
        print("B")
    elif w >= 0.7 :
        print("C")
    elif w >= 0.6 :
        print("D")
    elif w < 0.6 :
        print("F")
except ValueError:
    print("Bad Score")