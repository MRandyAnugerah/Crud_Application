import streamlit as st
from PIL import Image

def about_func():
    st.subheader("About Me")

    col1,col2 = st.columns(2)
    image = Image.open("a.jpeg")
    col1.image(image,
               caption='M. Randy Anugerah',
               use_column_width=True
               )
    with col2:
        st.write("You can check my Portofolio in this website:")
        st.write("[Check out my website](https://randyanugerah27030.wixsite.com/my-site-3)")
        st.write("You can check all my project and want i do:")
        st.write("[Check out my github](https://github.com/MRandyAnugerah)")
        st.write("And you can check my linkedln:")
        st.write("[Check out my linkedln](https://www.linkedin.com/in/m-randy-anugerah-017879217/)")

        