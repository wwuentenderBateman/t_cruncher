import streamlit as st
from scipy.stats import t

st.title("t-critical calculator")

alpha = st.number_input("Signifikanzniveau (α)", min_value=0.001, max_value=0.5, value=0.05, step=0.01)
df = st.number_input("Freiheitsgrade (df)", min_value=1, value=1000, step=1)
tail = st.selectbox("Testart", ["zweiseitig", "einseitig"])

if tail == "zweiseitig":
    t_crit = t.ppf(1 - alpha / 2, df)
else:
    t_crit = t.ppf(1 - alpha, df)

st.write(f"**t-kritischer Wert:** ±{round(t_crit, 3)}")