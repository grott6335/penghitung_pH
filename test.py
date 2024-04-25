import streamlit as st

st.header('Penentuan p4H', divider='rainbow')

angka_pertama = st.number_input('molaritas')
st.write('The first number is ', angka_pertama)

angka_kedua = st.number_input('valensi')
st.write('ph', angka_kedua)

operasi_matematika = angka_pertama * angka_kedua
st.write(f"molaritas {angka_pertama} x ph {angka_kedua} = OH {operasi_matematika}")
