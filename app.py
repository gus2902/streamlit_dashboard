import streamlit as st

st.title('Hello streamlit')
st.header('this is header')
st.subheader('this is subheader')

col1, col2 = st.columns([2,3])
with col1:
    st.subheader('col1 입니다')
with col2:
    st.subheader('col2 입니다')