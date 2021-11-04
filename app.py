import streamlit as st
import pandas as pd

def landpage():
    st.title("To Do App My Work")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
import streamlit as st
import pandas as pd
from database import create_data, create_table

def landpage():
    st.title("To Do App My Work")

    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    create_table()

    if choice == "Create":
        st.subheader("Add Work")
        work = st.text_area("Work to do")
        work_status = st.selectbox("Status Work", ["Proses","Waiting","Done"])
        work_due_date = st.date_input("Due Date Work")

        if st.button("Create Work"):
            create_data(work, work_status, work_due_date)
            st.success("Successfully Create new Work: {}".format(work))
        
    elif choice == "Read":
        st.subheader("View My Work")

    elif choice == "Update":
        st.subheader ("Edit My Work")

    elif choice == "Delete":
        st.subheader ("Delete My Work")  
          
    else:
        st.subheader("Check Me")

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
