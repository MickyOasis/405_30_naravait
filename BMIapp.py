import streamlit as st
st.markdown("# :blue[🩺❤️คำนวลค่าBMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ")
weight = st.number_input("กรอกน้ำหนักของคุณ (kg):", min_value=0.0 , value=0.0)
height_cm = st.number_input("กรอกส่วนสูงของคุณ (Meter):", min_value=0.0 , value=0.0)
if st.button("คำนวลค่า BMI 💪"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)
  st.write("---")
  st.header(f"ค่า BMI ของคุณคือ: {bmi:.2f}")
  if bmi < 18.5:
    st.warning("⚠️คุณผอมเกินไป")
  elif 18.5 <= bmi < 23.0:
    st.success("🎉คุณสมส่วน")
  elif 23.0 <= bmi < 25.0:
    st.info("🔔คุณท้วม")
  else:
    st.error("🚨คุณอยู่ในเกณฑ์อ้วน ควรไปออกกำลังกาย")

st.divider()
st.write("นายนราวิชญ์ หน่อสุวรรณ เลขที่ 30  ม.4/5")
