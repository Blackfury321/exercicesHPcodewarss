def magicnumber(pair):
    n1 = 2
    while pair > 0:
        if n1 % 2 != 0:
            print(f"[{n1} : {n1*2}]", end=" ") 
            pair -= 1
        n1 += 1

pair = int(input())

magicnumber(pair)

