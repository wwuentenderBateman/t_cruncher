import streamlit as st
from scipy.stats import t
import numpy as np
import pandas as pd
# pip install fpdf
from io import BytesIO
from fpdf import FPDF

st.title("one-sample t-test calculator")

# Eingaben
uploaded_file = st.file_uploader("CSV- oder Excel-Datei hochladen oder manuell eingeben", type=["csv", "xlsx"], key="csv_or_excel_upload_tcruncher")
data_input = st.text_area("Oder gib deine Stichprobe manuell ein (z. B. 230, 245, 240):")
hypo_mean = st.number_input("Erwarteter Mittelwert (μ)", value=250.0)
alpha = st.number_input("Signifikanzniveau (α)", min_value=0.001, max_value=0.5, value=0.05, step=0.01, format="%.3f")
tail = st.selectbox("Testart", ["zweiseitig", "einseitig größer", "einseitig kleiner"])

# Datenverarbeitung
import os
data = None
if uploaded_file:
    try:
        filename = uploaded_file.name
        ext = os.path.splitext(filename)[1].lower()

        if ext == ".csv":
            df_csv = pd.read_csv(uploaded_file, header=None)
        elif ext == ".xlsx":
            df_csv = pd.read_excel(uploaded_file, header=None, engine="openpyxl")
        else:
            st.warning("❌ Nicht unterstützter Dateityp.")
            df_csv = None

        if df_csv is not None:
            data = pd.to_numeric(df_csv.iloc[:, 0], errors='coerce').dropna().to_numpy()
    except Exception as e:
        st.warning(f"⚠️ Fehler beim Einlesen: {e}")
elif data_input:
    try:
        data = np.array([float(x.strip()) for x in data_input.split(",")])
    except:
        st.warning("⚠️ Bitte gib gültige Zahlen ein, getrennt durch Kommas.")

if data is not None and len(data) > 1:
    n = len(data)
    sample_mean = np.mean(data)
    sample_std = np.std(data, ddof=1)
    df = n - 1
    t_stat = (sample_mean - hypo_mean) / (sample_std / np.sqrt(n))

    if tail == "zweiseitig":
        t_crit = t.ppf(1 - alpha / 2, df)
        reject = abs(t_stat) > t_crit
    elif tail == "einseitig größer":
        t_crit = t.ppf(1 - alpha, df)
        reject = t_stat > t_crit
    elif tail == "einseitig kleiner":
        t_crit = t.ppf(alpha, df)
        reject = t_stat < t_crit

    st.markdown("### 📊 Ergebnisse")
    st.write(f"Stichprobenmittelwert: {sample_mean:.3f}")
    st.write(f"Standardabweichung (s): {sample_std:.3f}")
    st.write(f"t-Wert: {t_stat:.3f}")
    st.write(f"t-kritisch: ±{t_crit:.3f}")
    st.write(f"Freiheitsgrade: {df}")

    if reject:
        st.error("🚫 H₀ wird abgelehnt.")
    else:
        st.success("✅ H₀ kann nicht abgelehnt werden.")

#Plot
import matplotlib.pyplot as plt
import seaborn as sns

# Plot nur anzeigen, wenn Daten vorhanden
if data is not None and len(data) > 1:
    x = np.linspace(-4, 4, 1000)
    y = t.pdf(x, df)

    fig, ax = plt.subplots()
    sns.lineplot(x=x, y=y, ax=ax)

    # kritische Grenzen
    if tail == "zweiseitig":
        t_left = -t_crit
        t_right = t_crit
        ax.fill_between(x, y, where=(x <= t_left) | (x >= t_right), color='red', alpha=0.3, label="kritischer Bereich")
    elif tail == "einseitig größer":
        ax.fill_between(x, y, where=(x >= t_crit), color='red', alpha=0.3, label="kritischer Bereich")
    elif tail == "einseitig kleiner":
        ax.fill_between(x, y, where=(x <= t_crit), color='red', alpha=0.3, label="kritischer Bereich")

    # berechneter t-Wert
    ax.axvline(t_stat, color='black', linestyle='--', label=f"t = {t_stat:.2f}")

    ax.set_title("t-Verteilung")
    ax.legend()
    st.pyplot(fig)

    # PDF Export
    st.markdown("### 📄 PDF-Export")
    if st.button("PDF mit Ergebnissen herunterladen"):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)
        pdf.cell(200, 10, txt="One-Sample T-Test Ergebnisse", ln=True, align="C")
        pdf.ln(10)
        pdf.cell(200, 10, txt=f"Stichprobenmittelwert: {sample_mean:.3f}", ln=True)
        pdf.cell(200, 10, txt=f"Standardabweichung (s): {sample_std:.3f}", ln=True)
        pdf.cell(200, 10, txt=f"t-Wert: {t_stat:.3f}", ln=True)
        pdf.cell(200, 10, txt=f"t-kritisch: ±{t_crit:.3f}", ln=True)
        pdf.cell(200, 10, txt=f"Freiheitsgrade: {df}", ln=True)
        entscheidung = "H0 wird abgelehnt" if reject else "H0 kann nicht abgelehnt werden"
        pdf.cell(200, 10, txt=f"Entscheidung: {entscheidung}", ln=True)

        # PDF als Download bereitstellen
        try:
            pdf_data = pdf.output(dest='S').encode('latin1')
            st.download_button(
                label="PDF herunterladen",
                data=pdf_data,
                file_name="t_test_ergebnisse.pdf",
                mime="application/pdf"
            )
        except Exception as e:
            st.error(f"❌ Fehler beim PDF-Export: {e}")

    # Plot als PNG-Download
    st.markdown("### 🖼️ Plot herunterladen")
    img_buffer = BytesIO()
    fig.savefig(img_buffer, format="png")
    st.download_button(
        label="Plot als PNG herunterladen",
        data=img_buffer.getvalue(),
        file_name="t_test_plot.png",
        mime="image/png"
    )