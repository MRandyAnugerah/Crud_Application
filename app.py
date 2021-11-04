import streamlit as st
from db import create_table
from create import create_func
from read import read_func
from update import update_func

def landpage():
    st.title("To Do App My Work")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        create_func()
        
    elif choice == "Read":
        read_func()

    elif choice == "Update":
        update_func()

    elif choice == "Delete":
        st.subheader ("Delete My Work")  
          
    else:
        st.subheader("Check Me")
     
