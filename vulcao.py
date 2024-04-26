while True:
    t = int(input())
    p = int(input())
    if p == 0 and t == 0:
        break
    elif p > t:
        print("ALARME")
    else:
        print("O Havai pode dormir tranquilo")