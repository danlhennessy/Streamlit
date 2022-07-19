import streamlit as st
import numpy as np
import pandas as pd

st.title("My Monthly Budget")

outgoings = np.array([])
incomings = np.array([])
class incoming():
    def __init__(self, value):
        self.value = value
        
class outgoing:
    def __init__(self, value):
        self.value = value
        
    
        
totalin = incoming(0)
totalout = outgoing(0)

def listout(newout):
    temp = np.append(outgoings, newout)
    return temp

def listin(newin):
    temp = np.append(incomings, newin)
    return temp
        
class subin(incoming):
    def __init__(self, type, value):
        super().__init__(value)
        self.type = type
        totalin.value += self.value
        global incomings # Bring in global incomings variable
        incomings = listin(self) # Append new income object to np array ('incomings')
    
    def adjust(self, newval):
        totalin.value += (newval - self.value)
        self.value = newval

class subout(outgoing):
    def __init__(self, type, value):
        super().__init__(value)
        self.type = type
        totalout.value += self.value
        global outgoings 
        outgoings = listout(self) 
        
    def adjust(self, newval):
        totalout.value += (newval - self.value)
        self.value = newval

pay = subin('salary', 1200)

groceries = subout('food', 200)

def calcleftover():
    left = totalin.value - totalout.value
    return left
    

#groceries.adjust(int(input("Change budget to: ")))
print(groceries.value)
print(calcleftover())

for v in outgoings:
    print(f"Outgoings: {v.type}, £{v.value}")
    
for v in incomings:
    print(f"Incomings: {v.type}, £{v.value}")
    
df = pd.DataFrame({"In" : incomings, "Out" : outgoings})  # Need new list with vals..
print(df)