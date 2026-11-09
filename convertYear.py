import streamlit as st
st.title("แอพิเคชั่นแปลงปี พ.ศ. เป็น ค.ศ.")
bh_year=st.number_input("กรอกปี พ.ศ. ที่ต้องการแปลง",value=2569)
ceyear=bh_year-543
st.header(f"ปี ค.ศ. คือ : {ce_year}")
