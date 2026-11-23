import streamlit as st
st.title("แอปพลิเคชั่นส่วนลด และ ค่าvat")
price = st.number_input("กรอกราคาสินค้า (บาท):", min_value=0.0 , value=0.0)
saleprice = st.number_input("กรอกส่วนลด (%):", min_value=0.0 , value=0.0)
saleprice = price*saleprice/100
vat = price*0.07
net_price = saleprice - vat
st.header(f"• ราคาสินค้า: {price:.2f} บาท")
st.header(f"• เปอร์เซ็นส่วนลด: {sale:.2f} %")
st.header(f"• ส่วนลด: {saleprice:.2f} บาท")
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคาสุทธิ: {net_price:.2f} บาท")
st.divider()
st.write("นายนราวิชญ์ หน่อสุวรรณ เลขที่ 30  ม.4/5")
