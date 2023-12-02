
import streamlit as st

st.set_page_config(
    page_title="my profile|yuni",
    page_icon="🧕",
    layout="wide"
)
st.title("WELCOME TO MY PORTFOLIO 🧕")

st.sidebar.success("PORTOFOLIO")

from PIL import Image

st.title('PROFILE👩‍🎓')


image = Image.open('image02.jpg')
st.image(image, width=500)
st.subheader("NAMA : YUNI SULISTIAWATI")
st.caption("NIM : 0402201082")
st.markdown('''
            - Tempat Tanggal Lahir : Brebes 14 juli  2001
            - Alamat               : Sengon Tanjung  Brebes
            - Hobi                 : ngutak ngatik
            - Cita-cita            : big boss :)
            - Hal yang disukai     : TIDUR
            - Status               : Sudah punya hehe
            """
            ''')


st.markdown('## Tentang Saya', unsafe_allow_html=True)
st.info('''
        nama saya yuni sulistiawati, biasa dipanggil yuni atau sulis aja..
        saya dari prodi "TEKNIK INFORMATIKA" dari perkuliahan UNIVERSITAS NAHDLATUL ULAMA CIREBON
        dulu saya mendengar mahasiswa prodi teknik informatika itu seperti susah dan berat
        namun bagi saya juga memang begitu,;) tapi seru juga,
        ''')

st.header("*THANK YOU*")

