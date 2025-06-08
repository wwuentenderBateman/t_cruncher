try:
    import pandas as pd
    import xlsxwriter
    from io import BytesIO
    pandas_xlsxwriter_available = True
except ImportError:
    pandas_xlsxwriter_available = False

import streamlit as st

# Excel-Vorlage Download-Block
st.title("Excel-Vorlage herunterladen")
st.write("Diese Excel-Tabelle kann heruntergeladen werden, um sie zu befüllen und anschließend im t-cruncher hochzuladen.")
st.write("Eine Excel-Tabelle ist für die meisten User angenehmer, als eine CSV-Datei zu erstellen oder die Werte manuell"
         " in das Textfeld einzutippen.")
st.write("Bitte achte darauf, die Tabelle nicht zu verändern oder zu formatieren, sondern nur zu befüllen.")
st.write("Klicke den Button, um die Tabelle herunterzuladen.")
if not pandas_xlsxwriter_available:
    st.warning(
        "Bitte installiere die benötigten Pakete für den Excel-Export:\n\n"
        "```bash\npip install pandas xlsxwriter\n```"
    )
else:
    df_template = pd.DataFrame({"Werte": []})
    excel_buffer = BytesIO()
    with pd.ExcelWriter(excel_buffer, engine='xlsxwriter') as writer:
        df_template.to_excel(writer, index=False, sheet_name='Daten')
        worksheet = writer.sheets['Daten']
        worksheet.set_column('B:XFD', None, None, {'hidden': True})

    st.download_button(
        label="Excel-Vorlage herunterladen",
        data=excel_buffer.getvalue(),
        file_name="t_cruncher_vorlage.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
