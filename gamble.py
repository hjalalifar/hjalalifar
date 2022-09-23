# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 12:47:40 2022

@author: Asus
"""
arrivals=['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', "Ford"]
def fashionably_late(arrivals, name):
    
    order = arrivals.index(name)
    return order >= len(arrivals) / 2 and order != len(arrivals) - 1
fashionably_late(arrivals,Ford)