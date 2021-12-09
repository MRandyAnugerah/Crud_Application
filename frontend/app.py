import streamlit as st
from backend.db import create_table
from frontend.create import create_func
from frontend.read import read_func
from frontend.update import update_func
from frontend.delete import delete_func
from frontend.about import about_func

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
        about_func()
     
