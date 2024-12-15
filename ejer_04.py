number = int(input())
five = 0
tree = 0
for i in range(number + 1): 
    if i % 3 == 0 and i % 5 == 0: 
        tree += 3 
        five += 3 
    elif i % 3 == 0: 
        tree += 1 
    elif i % 5 == 0: 
        five += 2 

if (five > tree):
    print("Five")
if (tree > five):
    print("Three")
if (tree == five):
    print("No one won")
