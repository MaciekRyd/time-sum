import streamlit as st
from datetime import timedelta

st.title("⏱️ Sumator czasu (gg:mm)")

st.write("Podawaj wartości czasu w formacie **gg:mm**, jedna po drugiej.")

# Inicjalizacja sesji
if 'czasy' not in st.session_state:
    st.session_state.czasy = []

# Formularz do dodawania nowego czasu
with st.form("formularz_czasu", clear_on_submit=True):
    nowy_czas = st.text_input("Nowy czas (gg:mm)")
    submitted = st.form_submit_button("Dodaj")

    if submitted:
        try:
            godziny, minuty = map(int, nowy_czas.strip().split(":"))
            if godziny < 0 or minuty < 0 or minuty >= 60:
                st.warning("Błąd: minuty muszą być w zakresie 0–59, a godziny nie mogą być ujemne.")
            else:
                st.session_state.czasy.append((godziny, minuty))
        except ValueError:
            st.error("Nieprawidłowy format. Użyj formatu gg:mm (np. 2:30)")

# Wyświetlanie wprowadzonych czasów
if st.session_state.czasy:
    st.subheader("Wprowadzone czasy:")
    for i, (g, m) in enumerate(st.session_state.czasy, 1):
        st.write(f"{i}. {g:02d}:{m:02d}")

    # Sumowanie
    total = timedelta()
    for g, m in st.session_state.czasy:
        total += timedelta(hours=g, minutes=m)

    # Wyświetlenie sumy
    total_godziny = total.seconds // 3600 + total.days * 24
    total_minuty = (total.seconds % 3600) // 60
    st.subheader(f"🟢 Suma czasu: {total_godziny:02d}:{total_minuty:02d}")
else:
    st.info("Nie dodano jeszcze żadnego czasu.")

# Przycisk resetujący
if st.button("🗑️ Wyczyść wszystko"):
    st.session_state.czasy = []