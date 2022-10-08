#!/usr/bin/env python
# coding: utf-8

# In[3]:


import random
def findNamesWithLetter(letter):
    with open("names.txt") as f:
        for i in f:
            if letter in i:
                print(i)
letter = str(random.choice("ertyioasghklbnm"))
print(f"Printing names with the letter {letter}")
findNamesWithLetter(letter)


# In[ ]:




