import streamlit as st
from backend.db import create_data

def create_func():
    st.subheader("Add Work")
    work = st.text_area("Work to do")
    work_status = st.selectbox("Status Work", ["Proses","Waiting","Done"])
    work_due_date = st.date_input("Due Date Work")

    if st.button("Create Work"):
        create_data(work, work_status, work_due_date)
        st.success("Successfully Create new Work: {}".format(work))