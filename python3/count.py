# write a program repeatedly

try:
    while True:
        w = int(input("Enter a number: "))
        count = 0
        total = None
        if total is None or w != 7:
            total = w
            count = count + 1
            print(w)
            print(total)
            print(count)
            continue
        elif w == 7:
            print('done')
            print(total, count, total/count)
            break
except ValueError:
    print("Invalid input")
