import streamlit as st

mylist = []
    #Initialise session state and set value to []
if 'test' not in st.session_state:
    st.session_state['test'] = []
a = [st.text_area("Enter New Outgoing: ")]
if a:
    st.session_state['test'] += a # When user inputs text, session state concatenates a list with that text to itself
st.session_state
mylist = st.session_state['test'][1:] # Display list minus the initial empty string in index 0
mylist