import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

DATA_PATH = r"C:\Users\DELL\Desktop\Datasets\pathologies_clean_final.csv"

@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)

df = load_data()

st.title("Pathologies Explorer — Clean dataset")
st.markdown("Interactive explorer: filter by country, cause, year and view trends.")

# sidebar filters
countries = sorted(df['country'].unique())
causes = sorted(df['cause'].unique())
selected_country = st.sidebar.selectbox("Country", options=["All"] + countries)
selected_cause = st.sidebar.selectbox("Cause", options=["All"] + causes)
year_range = st.sidebar.slider("Year range", int(df['year'].min()), int(df['year'].max()), (2010, 2019))

# filtering
mask = (df['year'] >= year_range[0]) & (df['year'] <= year_range[1])
if selected_country != "All":
    mask &= (df['country'] == selected_country)
if selected_cause != "All":
    mask &= (df['cause'] == selected_cause)

filtered = df[mask]

st.subheader("Summary")
st.write("Rows:", filtered.shape[0])
st.dataframe(filtered.head(50))

# simple plots
st.subheader("Trends")
trend = filtered.groupby('year').agg({'Number':'sum','Percent':'mean','Rate':'mean'}).reset_index()
fig, ax = plt.subplots(1,1, figsize=(8,4))
ax.plot(trend['year'], trend['Number'])
ax.set_title("Number trend")
ax.set_xlabel("Year")
ax.set_ylabel("Number")
st.pyplot(fig)

st.subheader("Top causes (in filtered set)")
top = filtered.groupby('cause')['Number'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top)
