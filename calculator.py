import streamlit as st

# Judul aplikasi
st.title("Kalkulator Sederhana")

# Input angka pertama
num1 = st.number_input("Masukkan angka pertama:", value=0)

# Input angka kedua
num2 = st.number_input("Masukkan angka kedua:", value=0)

# Pilihan operasi
operation = st.selectbox("Pilih operasi:", ["+", "-", "*", "/"])

# Tombol untuk menghitung
if st.button("Hitung"):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Pembagian dengan nol tidak boleh"
    st.success(f"Hasil: {result}")
