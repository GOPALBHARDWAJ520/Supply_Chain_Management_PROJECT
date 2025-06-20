#streamlit run advanced_dashboard.py

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Supply Chain Insights", layout="wide")

# Load data
df = pd.read_csv("supply_chain_data.csv")
df.dropna(inplace=True)

# Sidebar filters
st.sidebar.header("🔍 Filter Data")
product_types = st.sidebar.multiselect("Select Product Type", df['Product type'].unique(), default=df['Product type'].unique())
suppliers = st.sidebar.multiselect("Select Supplier", df['Supplier name'].unique(), default=df['Supplier name'].unique())
transport_modes = st.sidebar.multiselect("Select Transport Mode", df['Transportation modes'].unique(), default=df['Transportation modes'].unique())

# Filtered DataFrame
filtered_df = df[
    (df['Product type'].isin(product_types)) &
    (df['Supplier name'].isin(suppliers)) &
    (df['Transportation modes'].isin(transport_modes))
]

# KPIs
st.title("📦 Supply Chain Management Dashboard")
st.markdown("Real-time analytics for inventory, logistics, and manufacturing")

col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"${filtered_df['Revenue generated'].sum():,.0f}")
col2.metric("Total Costs", f"${filtered_df['Costs'].sum():,.0f}")
col3.metric("Products Sold", int(filtered_df['Number of products sold'].sum()))

# Row 1: Revenue vs Manufacturing Cost
st.subheader("💰 Revenue vs Manufacturing Cost by Product")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.scatterplot(data=filtered_df, x="Manufacturing costs", y="Revenue generated", hue="Product type", ax=ax1)
st.pyplot(fig1)

# Row 2: Stock Levels and Production Volumes
col4, col5 = st.columns(2)

with col4:
    st.subheader("📦 Stock Levels by Product Type")
    fig2, ax2 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x="Product type", y="Stock levels", ax=ax2)
    st.pyplot(fig2)

with col5:
    st.subheader("🏭 Production Volumes by Supplier")
    fig3, ax3 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=filtered_df, x="Supplier name", y="Production volumes", estimator='mean', ax=ax3)
    ax3.set_xticklabels(ax3.get_xticklabels(), rotation=45)
    st.pyplot(fig3)

# Row 3: Shipping and Transportation
col6, col7 = st.columns(2)

with col6:
    st.subheader("🚚 Shipping Costs by Carrier")
    fig4, ax4 = plt.subplots(figsize=(8, 5))
    sns.boxplot(data=filtered_df, x="Shipping carriers", y="Shipping costs", ax=ax4)
    ax4.set_xticklabels(ax4.get_xticklabels(), rotation=45)
    st.pyplot(fig4)

with col7:
    st.subheader("🚛 Transportation Mode Frequency")
    transport_counts = filtered_df["Transportation modes"].value_counts().reset_index()
    transport_counts.columns = ["Mode", "Count"]
    fig5, ax5 = plt.subplots(figsize=(8, 5))
    sns.barplot(data=transport_counts, x="Mode", y="Count", ax=ax5)
    st.pyplot(fig5)

# Row 4: Defect Rates by Product
st.subheader("🧪 Defect Rates by Product Type")
fig6, ax6 = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Product type", y="Defect rates", ax=ax6)
st.pyplot(fig6)

st.markdown("---")
st.caption("Created by Gopal Bhardwaj | Powered by Streamlit")
