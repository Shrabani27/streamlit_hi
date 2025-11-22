import streamlit as st
st.title("Smart Grocer Calculater App")
st.write("Enter the quantity")

rice_qty = st.number_input("Enter the quantity of rice")
sugar_qty = st.number_input("Enter the quantity of sugar")
oil_qty = st.number_input("Enter the quantity of oil")

rice_price_perkg = 60
sugar_price_perkg = 45
oil_price_perlit = 120

rice_total_price = rice_qty * rice_price_perkg
sugar_total_price = sugar_qty * sugar_price_perkg
oil_total_price = oil_qty * oil_price_perlit

total_price = rice_total_price + sugar_total_price + oil_total_price

if total_price > 500:
    discount = total_price *0.10
else:
    discount = "No discount"

final_amount = total_price - discount

st.header("Bill details")
st.write("Total before discount: ₹{:.2f}".format(total_price))
st.write("Discount applied: ₹{:.2f}".format(discount))
st.write("Final amount to pay: ₹{:.2f}".format(final_amount))
