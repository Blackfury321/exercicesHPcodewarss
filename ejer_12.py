ordens = str(input().upper()).strip().split(" ")

initial = 0  

D = +0.2
E = -0.1
T = -0.05
P = -0.08


for i in ordens:
    if i == "D":
        initial += D
    if i == "E":
        initial += E
    if i == "T":
        initial += T
    if i == "P":
        initial += P

initial = round(initial, 2)
if initial >= 0.5:
    print(f"Oh no! His BAC is {initial} g/L and over the limit! He will not be able to give the speech!")
else:
    print(f"His BAC is {initial} g/L which is under the limit. He will be able to give the speech! Get ready!")