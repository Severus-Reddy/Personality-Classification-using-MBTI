import streamlit as st

st.set_page_config(
    page_title="Home",
    page_icon="👋",
)
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://images.unsplash.com/photo-1498932042873-e35fb6535a02?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1yZWxhdGVkfDE0fHx8ZW58MHx8fHw%3D&w=1000&q=80");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.write("# Welcome to Personality Classification! 👋")