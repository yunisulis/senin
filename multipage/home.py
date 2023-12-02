
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

import streamlit as st

st.title("")



st.header(":mailbox: Give this email a message")



   
contact_form = """
    <form action="https://formsubmit.co/yunsulisyun@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
         <input type="message" name="your message here" placeholder="message" required>
        </textarea>
        <button type="submit">Send</button>
    </form>
    """
st.markdown(contact_form, unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}<style>", unsafe_allow_html= True)
        
        local_css("style/style.css")
        
        
st.title("")

        

st.title("BEBERAPA JENJANG PENDIDIKAN YANG SAYA LALUI SELAMA MASA HIDUP")


st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("SDN Sengon 03")
   
with col2:
    st.subheader("MTs Plus AL Bukhori")
    
with col3:
    st.subheader("MA Plus AL Bukhori")
   
with col4:
    st.subheader("UNU Rombel AL Bukhori")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("sd.png", width= 190)
with col2:
   
    st.image("mts.png", width= 190)
with col3:
    
    st.image("ma.png", width= 190)
with col4:
    
    st.image("unuu.png", width= 190)



import streamlit as st



st.title("Pengalaman Organisasi✨")
st.write("Hanya Satu Organisasi Yang Saya Ikuti; ")

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("PANITIA ALFIYAH IBNU MALIK TAHUN 2020")


st.image("alfiah.jpg", width=500)

st.container()
col1, = st.columns(1)
with col1:
    st.subheader("Menjadi Panitia Dekdok Dekorasi Dokumentasi")




import streamlit as st



st.set_page_config(
    page_title="medsos | YUNI",
    page_icon="♥️",
    layout="wide"
)
st.title("MY MEDIA SOCIAL ")
st.subheader("don't forget follow me guys👇")


st.container()
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.subheader("INSTAGRAM")
   
with col2:
    st.subheader("FACEBOOK")
    
with col3:
    st.subheader("YOUTUBE")
   
with col4:
    st.subheader("TIKTOK")
   
st.container()
st.write("---")
col1, col2, col3, col4 = st.columns(4)
with col1:
   
    st.image("ig.png", width= 100)
    st.link_button("my instagram", "https://www.instagram.com/")
with col2:
   
    st.image("fb.png", width= 100)
    st.link_button("my facebook", "https://www.facebook.com/")
with col3:
    
    st.image("yu.png", width= 100)
    st.link_button("my youtube", "https://www.youtube.com/channel/UCNFvQMw9AZnUTIjaRjtLu0Q")
with col4:
    
    st.image("tik.jpg", width= 100)
    st.link_button("my tiktok", "https://www.tiktok.com/")




