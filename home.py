import streamlit as st

st.title("Willkommen bei t-cruncher")
st.write("Wähle oben links eine Seite aus dem Menü.")
st.write("Diese Anwendung entstand im Rahmen der Marketing-Vorlesung zum Thema Causal Research und bietet dir eine praktische Möglichkeit, t-kritische Werte sowie einfache t-Tests direkt im Browser durchzuführen."
         " t-cruncher soll dabei helfen, Hypothesentests – insbesondere One-Sample t-Tests – intuitiv, interaktiv und fehlerfrei umzusetzen. Ob zur Vorbereitung von Experimenten, zur Analyse von Befragungen oder als Lernhilfe für Statistik-Klausuren:"
         " Diese Seite unterstützt dich bei datenbasierten Entscheidungen.")

# Zusätzliche erklärende Abschnitte
st.markdown("### ℹ️ Was sind Freiheitsgrade (df)?")
st.write("Die Freiheitsgrade (engl. *degrees of freedom*, abgekürzt **df**) geben an, wie viele Werte in deiner Stichprobe **frei variieren können**, ohne dass eine feste Bedingung (z. B. der Mittelwert) verletzt wird. "
         "Beim **One-Sample t-Test** berechnet man df als: `df = n - 1`. Dabei ist **n** die Anzahl deiner Beobachtungen. Freiheitsgrade beeinflussen die Form der t-Verteilung – bei kleinen Stichproben ist sie breiter, bei großen ähnelt sie der Normalverteilung.")

st.markdown("### ℹ️ Was ist das Signifikanzniveau (α)?")
st.write("Das Signifikanzniveau (**α**) legt fest, **wie wahrscheinlich ein Fehler 1. Art** (fälschliches Ablehnen der Nullhypothese) **noch akzeptabel ist**. Typische Werte sind: 0,05 → 5 % Fehlerwahrscheinlichkeit, 0,01 → 1 % Fehlerwahrscheinlichkeit. "
         "Je kleiner α, desto **strenger** ist dein Test. Das Signifikanzniveau bestimmt auch die **Grenzen für den kritischen Bereich** – also, wann ein Ergebnis als „statistisch signifikant“ gilt.")