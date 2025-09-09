
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("PSAT/PreACT Score and Percentile Dashboard")

# Load data
df = pd.read_csv("filtered_psat_preact_2028_2029.csv")

# Rename columns for easier access
df.columns = ["Identifier", "Class", "Total", "ReadingWriting", "Math", "TotalPercentile", "Composite", "MathPreACT", "Science", "English", "ReadingPreACT"]

# Melt data for plotting
df_melted = df.melt(id_vars=["Class"], 
                    value_vars=["Total", "ReadingWriting", "Math", "Composite", "MathPreACT", "Science", "English", "ReadingPreACT"],
                    var_name="Subject", value_name="Score")
df_melted = df_melted.dropna()

# Subject filter
subjects = st.multiselect("Select subjects to display:", options=df_melted["Subject"].unique(), default=df_melted["Subject"].unique())
filtered_df = df_melted[df_melted["Subject"].isin(subjects)]

# Plot
fig = px.box(filtered_df, x="Class", y="Score", color="Subject",
             title="Score and Percentile Distribution by Subject and Class Year")
st.plotly_chart(fig)

# Show data table
st.subheader("Underlying Data Table")
st.dataframe(df)
