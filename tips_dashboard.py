import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# r to ensure that is for a path
# uploaded_file = r"data\tips.csv"
uploaded_file = r"data/tips.csv"
data= pd.read_csv(uploaded_file)
print(data)

st.title('Data Analysis on Tips Dataset')

st.header("data overview")
st.write("first few rows of the data set")
st.dataframe(data.head())

# data summary
st.header("data summary")
st.dataframe(data.describe())

# select columns for visualization
st.header("select columns for visualization")
x_axis = st.selectbox("x axis", data.columns)
y_axis = st.selectbox("y axis", data.columns)

plot_type= st.radio("select plot type: ", ["scatter plot","line plot","histogram plot"])

if plot_type == "scatter plot":
    st.subheader("scatter plot")
    fig= plt.figure()
    sns.scatterplot( x=x_axis, y=y_axis, data=data)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "histogram plot":
    st.subheader("histogram plot")
    fig= plt.figure()
    sns.histplot( x=x_axis, data=data)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)
elif plot_type == "line plot":
    st.subheader("line plot")
    fig= plt.figure()
    sns.lineplot( x=x_axis,y=y_axis, data=data)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    st.pyplot(fig)


st.header("correlation heatmap")
if st.button ("Generate Heatmap"):
    fig = plt.figure()
    sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="Blues")
    st.pyplot(fig)

st.write("explore and analys data")
