import numpy as np
import pandas as pd
import scipy
import streamlit as st
import plotly.express as px

st.title("Age/Strength correlation in powerlifting")

# Data from http://old.openpowerlifting.org/data.html

df = pd.read_csv('D:\Backup\Work\DevOps\Programming\Streamlit\correlation\entries.csv')


# df cleanup:
weightclass_ninety = df[df['WeightClassKg'] == '90']
deadlift_ninety = weightclass_ninety[['Age', 'Best3DeadliftKg']].dropna(axis=0)
deadlift_ninety['Best3DeadliftKg'] = deadlift_ninety['Best3DeadliftKg'].abs()
deadlift_ninety.rename(columns={'Best3DeadliftKg': 'Deadlift 1RM (kg)'}, inplace=True)

fig = px.scatter(deadlift_ninety, x='Age', y='Deadlift 1RM (kg)')
st.plotly_chart(fig)