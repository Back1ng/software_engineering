a = int(input())
if a < 0 or a > 10:
    print("Input values less then 0 or more then 10")
    exit()
elif a <= 3:
    print("0-3")
elif a > 3 and a <= 6:
    print("3-6")
elif a > 6:
    print("6-10")