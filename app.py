import streamlit as st
import pandas as pd

def landpage():
    st.title("To Do App My Work")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        st.subheader("Add Work")
        
    elif choice == "Read":
        st.subheader("View My Work")

    elif choice == "Update":
        st.subheader ("Edit My Work")

    elif choice == "Delete":
        st.subheader ("Delete My Work")  
          
    else:
        st.subheader("Check Me")
