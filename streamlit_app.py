import streamlit as st
#x = st.slider('x')  # 👈 this is a widget
#st.write(x, 'squared is', x * x)

import cx_Oracle

connection = cx_Oracle.connect(
    user="demopython",
    password="XXXXX",
    dsn="localhost/xepdb1")

st.write("Successfully run with CX Oracle")
