try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie




st.set_page_config(page_title="Dillon King", page_icon="🖥", layout="wide")




def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ---- use local css ----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")


# ---- load assets ----

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_w51pcehl.json")
powershell_image = Image.open("Images/download.jpg")


# ---- header section ----
with st.container():
    st.subheader("Hi, I'm Dillon")
    st.title("I'm an avid computer user who specilizes in microsoft windows and python.")
    st.write("I love finding new ways to do things, expecialy at the command line I also use linux from time to time.")
    st.write("[Buy Me A Coffee](https://bmc.link/kingdillon)")
# ---- what I do ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""
        
        I am 14 so currently in school, my favourite subject is obviously computer science and with this my favourite things to do are:
        - Learn lots about windows 
        - Learn how to use powershell and cmdlets
        - use and learn linux
        - learn python
          
            
        """)
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- more of what I'm learning ----
with st.container():
    st.write("---")
    st.header("What I'm Learning")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(powershell_image)
    with text_column:
        st.subheader("""Learing windows powershell""")

# ---- contact ----  
with st.container():
    st.write("---")
    st.header("Get In Touch With Me")
    st.write("##")


    contact_form = """<form action="https://formsubmit.co/kingdillon88@outlook.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""  

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
        




