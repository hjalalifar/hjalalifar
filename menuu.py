# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 12:30:44 2022

@author: Asus
"""

def parseLine(line):
    h = line.partition("on sale")
    k = "on sale"
    for j in h:
        if j == k:
            print("ON SALE:", end="")
    start = line.find('"')
    end = line.find('"',start+1)   
    i = start
    while i <= end:
        print(line[i],end="")
        i += 1
    print()
with open("menu.txt") as f:
    for line in f:
        parseLine(line)
        