import streamlit as st

st.set_page_config(
    page_title="email | YUNI",
    page_icon="📩",
    layout="wide"
)

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