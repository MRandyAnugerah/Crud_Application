import streamlit as st
import pandas as pd
from db import create_table
from create import create_func

def landpage():
    st.title("To Do App My Work")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        create_func()
        
    elif choice == "Read":
        st.subheader("View My Work")

    elif choice == "Update":
        st.subheader ("Edit My Work")

    elif choice == "Delete":
        st.subheader ("Delete My Work")  
          
    else:
        st.subheader("Check Me")
     
