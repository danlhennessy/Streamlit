import streamlit as st
import pandas as pd
import numpy as np

st.title("Test App")

st.write("Hello World")

test1 = "Magic Test"

test1

sidebar = st.sidebar.write("I am in a sidebar?")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)