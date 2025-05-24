import streamlit as st
import pandas as pd
import plotly.express as px
from utils.load_data import load_data

st.set_page_config(page_title="Sales Dashboard", layout="wide")

# Load data
df = load_data("sales_data_sample.csv")

# Sidebar filters
st.sidebar.header("Filter")
months = st.sidebar.multiselect("Month:", df["MONTH"].unique())
regions = st.sidebar.multiselect("Region:", df["TERRITORY"].unique())

filtered_df = df.copy()
if months:
    filtered_df = filtered_df[filtered_df["MONTH"].isin(months)]
if regions:
    filtered_df = filtered_df[filtered_df["TERRITORY"].isin(regions)]

# KPIs
total_sales = round(filtered_df["SALES"].sum(), 2)
total_orders = filtered_df["ORDERNUMBER"].nunique()
units_sold = filtered_df["QUANTITYORDERED"].sum()

st.title("📊 Sales Dashboard")
st.markdown("## Key Performance Indicators")

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales ($)", f"{total_sales:,.2f}")
col2.metric("Total Orders", total_orders)
col3.metric("Units Sold", units_sold)

# Charts
st.markdown("## Sales by Product Line")
sales_by_product = (
    filtered_df.groupby("PRODUCTLINE")["SALES"].sum().reset_index()
)
fig1 = px.bar(sales_by_product, x="PRODUCTLINE", y="SALES", title="Sales by Product Line")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("## Monthly Sales Trend")
monthly_sales = (
    filtered_df.groupby("MONTH")["SALES"].sum().reset_index()
)
fig2 = px.line(monthly_sales, x="MONTH", y="SALES", title="Monthly Sales Trend")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("## Raw Data")
st.dataframe(filtered_df)
