names = input().split(",")
actions = input().split(",")
things = input().split(",")

for i in names:
    for n in actions:
        for a in things:
            print(f"{i} {n} {a}")
