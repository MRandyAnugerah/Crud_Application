import streamlit as st
from db import create_table, delete_work
from create import create_func
from read import read_func
from update import update_func
from delete import delete_func

def landpage():
    st.title("To Do App My Work")

    menu = ["Read", "Create", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()
        
    if choice == "Read":
        read_func()

    elif choice == "Create":
        create_func()

    elif choice == "Update":
        update_func()

    elif choice == "Delete":
        delete_func()
          
    else:
        st.subheader("Check Me")
     
