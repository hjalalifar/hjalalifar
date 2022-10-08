while True:
    
    s = input("give me a word: ")
    b = int(input("Give me a number: "))
    
    if b <= len(s):
        while b < len(s):    
            w = s[b]    
            print(w,"= " ,end="")
            print(s.count(w))
            b = b + 4
    else:
        print("your number is more than the number of the letter of the word")
    
