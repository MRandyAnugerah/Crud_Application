from backend.db import view_my_work
import streamlit as st
import plotly.express as px
import pandas as pd

def read_func():
    st.subheader("View My Work")
    result = view_my_work()
    df = pd.DataFrame(result, columns=['Work','Status','Due Date'])
    work_df = df['Status'].value_counts().to_frame()
    work_df = work_df.reset_index()
    st.dataframe(df)

    plot = px.pie(work_df, names="index", values="Status", hole=0.5, color_discrete_sequence=px.colors.sequential.RdBu )
    st.plotly_chart(plot)
    