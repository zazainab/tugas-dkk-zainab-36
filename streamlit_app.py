import streamlit as st

st.title("🧮 Aplikasi Penghitungan Sederhana")

# Input angka
angka1 = st.number_input("Masukkan angka pertama:", value=0.0)
angka2 = st.number_input("Masukkan angka kedua:", value=0.0)

# Pilih operasi
operasi = st.selectbox(
    "Pilih operasi:",
    ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"]
)

# Tombol hitung
if st.button("Hitung"):
    if operasi == "Tambah (+)":
        hasil = angka1 + angka2
    elif operasi == "Kurang (-)":
        hasil = angka1 - angka2
    elif operasi == "Kali (×)":
        hasil = angka1 * angka2
    elif operasi == "Bagi (÷)":
        hasil = angka1 / angka2 if angka2 != 0 else "Error: Pembagian dengan nol"

    st.subheader("Hasil:")
    st.write(f"**{hasil}**")
