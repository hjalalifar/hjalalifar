from random import randint
print("user")
x1 = randint(1,6)
if x1 == 21:
    print("user is winner")
while x1 <= 21:
    print(x1)
    answer = input("do you want to Continue:")
    w = len(answer)
    if w == 3:
        x1 = x1 + randint(1,6)    
    else:
        break

print("-------------------------------------------------------")

print("dealer")
x2 = randint(1,6)
if x2 == 21:
    print("dealer is winner")
while x2 <= 21:
    print(x2)
    answer = input("do you want to Continue:")
    w = len(answer)
    if w == 3:
        x2 = x2 + randint(1,6)  
    else:
        break

if x1 - 21 < x2 - 21:
    print("user is winner")
else:
    print("dealer is winner")
