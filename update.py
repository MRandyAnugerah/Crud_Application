import streamlit as st
import pandas as pd
from db import view_my_work, get_data, view_unique_work, update_data

def update_func():
    st.subheader("Update Data")
    result = view_my_work()
    df = pd.DataFrame(result, columns=['Work','Status','Due Date'])
    work_df = df['Status'].value_counts().to_frame()
    work_df = work_df.reset_index()
    st.dataframe(df)

    list_of_work = [i[0] for i in view_unique_work()]
    selected_work = st.selectbox("Pick work you Want to Update",list_of_work)
    selected_result = get_data(selected_work)

    if selected_result:
        work = selected_result[0][0]
        work_status = selected_result[0][1]
        work_due_date = selected_result[0][2]
        
        new_work = st.text_area("Update work to do")
        new_work_status = st.selectbox(work_status, ["Proses","Waiting","Done"])
        new_work_due_date = st.date_input("Update Due Date Work")

        if st.button("Update Work"):
            update_data(new_work, new_work_status, new_work_due_date, work, work_status, work_due_date)
            st.success("Successfully update '{}' to '{}'".format(work, new_work))

