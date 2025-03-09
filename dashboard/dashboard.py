import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

def load_data():
    return pd.read_csv("D:/Coding Camp/submission/dataset/reviews_sales_df.csv")
df = load_data()

if 'order_purchase_timestamp' in df.columns:
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

st.sidebar.title("Dashboard Filter")
selected_year = st.sidebar.selectbox("Pilih Tahun", df['order_purchase_timestamp'].dt.year.unique())

df_filtered = df[df['order_purchase_timestamp'].dt.year == selected_year]

st.title("Dashboard Pemesanan Produk")

st.header("Performa Pemesanan di Setiap Kota dan State")
city_orders = df_filtered["customer_city"].value_counts().head(10)
state_orders = df_filtered["customer_state"].value_counts().head(10)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].barh(city_orders.index[::-1], city_orders.values[::-1], color="skyblue")
ax[0].set_title("Jumlah Pemesanan per Kota")
ax[0].set_xlabel("Jumlah Pemesanan")

ax[1].barh(state_orders.index[::-1], state_orders.values[::-1], color="lightcoral")
ax[1].set_title("Jumlah Pemesanan per State")
ax[1].set_xlabel("Jumlah Pemesanan")

st.pyplot(fig)

st.header("Produk yang Paling Banyak dan Paling Sedikit Dipesan")
product_orders = df_filtered["product_category_name_english"].value_counts()

top_products = product_orders.sort_values(ascending=True).head(10)
bottom_products = product_orders.sort_values(ascending=False).head(10)

fig, ax = plt.subplots(1, 2, figsize=(14, 5))

ax[0].barh(top_products.index, top_products.values, color="seagreen")
ax[0].set_title("Produk yang Paling Banyak Dipesan")    
ax[0].set_xlabel("Jumlah Pemesanan")

# Bar chart produk tersedikit
ax[1].barh(bottom_products.index, bottom_products.values, color="tomato")
ax[1].set_title("Produk yang Paling Sedikit Dipesan")
ax[1].set_xlabel("Jumlah Pemesanan")
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()

st.pyplot(fig)
st.caption("Dibuat oleh: Mohammad Valeriant (MC-31)")