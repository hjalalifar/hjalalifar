
def askinput():
    letters = []
    letter = input("give me letters:")
    for i in letter:
        if i == " ":
            continue
        else:
            letters.append(i)
    return letters

with open("Iran.txt", "r") as f:
    letters = askinput()
    words = []
    for line in f:
        w = line.split()
        for j in w:
            for i in letters:
                if i in j:
                    words.append({i : j})
#separate keys of values
keys = []
for i in words:
    for key , value in i.items():
        keys.append(key)
#count keys
for i in letters: 
    print(i, end=" = ")
    w = keys.count(i)
    print(w)
# average of keys
average = len(words)/len(letters)
print(f"average = {average}")
    
    
