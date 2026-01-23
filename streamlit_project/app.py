import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Demo: Pandas + Visualization in Streamlit")

# Generate sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': np.random.randint(10, 100, 4)
})

st.subheader("Data Table")
st.dataframe(data)

# Create a bar plot
fig, ax = plt.subplots()
sns.barplot(x='Category', y='Values', data=data, palette='viridis', ax=ax)
st.subheader("Bar Plot Visualization")
st.pyplot(fig)

option = st.selectbox("Select category", data['Category'])
st.write(f"You selected {option}")
