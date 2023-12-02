
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

