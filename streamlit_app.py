import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("file_000000007ce061f7a22ac3d12b254176_conversation_id=67fbb908-a654-8013-9512-652d32bc7b5c&message_id=cfee5c1d-8cac-4ba7-bb49-1f42f7f90c1c.png", width=200) 


st.title("aplikasi sederhana") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("tulis sebuah Angka:", value=0, step=1) 

if (angka % 2) == 0:
    st.write(f"{angka} adalah bilangan genap") 
else:
    st.write(f"{angka} adalah bilangan ganjil") 
