import numpy as np
import pandas as pd
import scipy.stats
import streamlit as st
import plotly.express as px

st.title("Age/Strength correlation in powerlifting")
st.header(" ")

# Data from http://old.openpowerlifting.org/data.html

df = pd.read_csv('D:\Backup\Work\DevOps\Programming\Streamlit\correlation\entries.csv')


# df cleanup:
weightclass_ninety = df[df['WeightClassKg'] == '90']
deadlift_ninety = weightclass_ninety[['Age', 'Best3DeadliftKg']].dropna(axis=0)
deadlift_ninety['Best3DeadliftKg'] = deadlift_ninety['Best3DeadliftKg'].abs()
deadlift_ninety.rename(columns={'Best3DeadliftKg': 'Deadlift 1RM (kg)'}, inplace=True)

age_range = st.slider("Age Range", value=[7,90])
lower, upper = age_range

deadlift_ninety = deadlift_ninety[(deadlift_ninety.Age>=lower) & (deadlift_ninety.Age<=upper)]

# Coefficient calcs
ages = deadlift_ninety['Age'].to_numpy()
lifts = deadlift_ninety['Deadlift 1RM (kg)'].to_numpy()
pearson, spearman, kendalltau = scipy.stats.pearsonr(ages, lifts), scipy.stats.spearmanr(ages, lifts), scipy.stats.kendalltau(ages, lifts)

# Charts (Peak avg = 27 yrs)
fig = px.scatter(deadlift_ninety, x='Age', y='Deadlift 1RM (kg)', trendline="lowess", trendline_color_override="red")
st.plotly_chart(fig)

st.write(f"""Coefficients:\n 
        Pearson = {pearson[0]}\n
    Spearman = {spearman[0]}\n
    Kendalltau = {kendalltau[0]}
    """)
