def add_two_integers():
    x = int(input("x: "))
    y = int(input("y: "))
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")
add_two_integers()