import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("vit.jpg", width=200) 


st.title("aplikasi sederhana") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("tulis sebuah Angka:", value=0, step=1) 

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap") 
else:
    st.write(f"{angka} adalah bilangan ganjil") 
