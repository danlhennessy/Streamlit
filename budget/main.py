import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

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

def listout(newout): # Function for adding new outgoings to list
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
        global incomings # Bring in global variable incomings 
        incomings = listin(self) # When a new object is created, call the listin function to update global var incomings
    
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



with st.sidebar:
    #Initialise session state and set value to []
    if 'outs' not in st.session_state and 'vals' not in st.session_state:
        st.session_state['outs'] = []
        st.session_state['vals'] = []
    a = [st.text_area("Enter New Outgoing: ")]
    b = [st.number_input("Value: ")]
    # When user inputs text, session state concatenates a list with that text to itself
    if st.button("submit"):
        st.session_state['outs'] += a
        st.session_state['vals'] += b
    #st.session_state
    # Combines session state lists for text/num box into a dict
    mydict = dict(zip(st.session_state['outs'], st.session_state['vals']))
    
    for key,value in mydict.items():
        temp = subout(key, value)


pay = subin('salary', 1200)

refunds = subin('misc', 50)

groceries = subout('food', 200)

rent = subout('rent', 500)

def calcleftover():
    left = totalin.value - totalout.value
    return left
endtotal = calcleftover()    

#groceries.adjust(int(input("Change budget to: ")))


for v in outgoings:
    print(f"Outgoings: {v.type}, £{v.value}")
    
for v in incomings:
    print(f"Incomings: {v.type}, £{v.value}")

outvals = invals = outtype = intype = np.array([])
for v in outgoings:
        outvals = np.append(outvals, v.value)
        outtype = np.append(outtype, v.type)
        
for v in incomings:
        invals = np.append(invals, v.value)
        intype = np.append(intype, v.type)

        
outdf = pd.DataFrame({"Out" : outvals, "Type" : outtype})
indf = pd.DataFrame({"In" : invals, "Type" : intype})


# Plotly Pie Charts
fig1 = px.pie(outdf, values = 'Out', names = 'Type')

fig2 = px.pie(indf, values = 'In', names = 'Type')

col1, col2, col3 = st.columns(3)
col1.markdown('Outgoing DataFrame')
col1.write(outdf)
col1.subheader("Outgoings")
col1.plotly_chart(fig1)

col2.markdown('Incoming DataFrame')
col2.write(indf)

col3.metric('Total Leftover (£)', endtotal)
#col2.plotly_chart(fig2)