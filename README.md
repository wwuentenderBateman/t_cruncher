# t_cruncher

Ein Tool zur Berechnung kritischer t-Werte.  
## Setup
```bash
pip install -r requirements.txt
python src/main.py---

### ✅ **2. `.gitignore`**
Versteckt unnötige Dateien (z. B. `.idea/`, `__pycache__/`, `.DS_Store`):

```bash
# Python
__pycache__/
*.pyc

# macOS
.DS_Store

# IDEs
.idea/
*.iml

# t_cruncher

📊 **t_cruncher** ist ein interaktives Streamlit-Tool zur Berechnung kritischer t-Werte, Durchführung von t-Tests sowie zum Einlesen und Auswerten von CSV- und Excel-Dateien.

## 🔧 Features
- Berechnung des kritischen t-Werts anhand von Freiheitsgraden & Signifikanzniveau
- Einfache t-Test Berechnung über Upload-Funktion
- Unterstützung für `.csv` und `.xlsx` (Excel)
- Bereitstellung einer Excel-Vorlage mit nur einer Spalte
- Export von Ergebnissen als PDF
- Übersichtliche Benutzeroberfläche mit Navigation über mehrere Seiten

## 🚀 Live-Demo
👉 [Zur App auf Streamlit Cloud](https://t-cruncher.streamlit.app/)

## 🖥️ Lokale Ausführung
1. Repository klonen:
   ```bash
   git clone https://github.com/wwuentenderBateman/t_cruncher.git
   cd t_cruncher
   ```

2. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

3. App starten:
   ```bash
   streamlit run pages/home.py
   ```

## 📁 Struktur
```
t_cruncher/
├── pages/
│   ├── home.py                  # Startseite mit Einleitung & Erklärung
│   ├── t_cruncher.py            # Hauptfunktion zum t-Wert berechnen
│   ├── excel-template 4 t-cruncher.py # Excel-Upload & Vorlage
├── requirements.txt
├── README.md
```

## 🧠 Hintergrund
Das Projekt entstand im Rahmen einer Marketing-Vorlesung mit Fokus auf kausaler Forschung. Ziel war es, Statistik zugänglicher zu machen.


---