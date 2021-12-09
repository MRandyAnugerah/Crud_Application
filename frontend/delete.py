import streamlit as st
import pandas as pd
from backend.db import delete_work, view_my_work, view_unique_work

def delete_func():
    st.subheader ("Delete My Work") 
    result = view_my_work()
    df = pd.DataFrame(result, columns=['Work','Status','Due Date'])
    st.dataframe(df) 

    list_of_work = [i[0] for i in view_unique_work()]
    selected_work = st.selectbox("Pick work you Want to Delete ??",list_of_work)
    st.warning("Do you want to delete {}".format(selected_work))
    if st.button("Delete work"):
        delete_work(selected_work)
        st.success("Data has being succesfully delete")