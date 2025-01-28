import streamlit as st
import webbrowser


st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


st.set_page_config(page_title="Mental Health", layout="wide")

st.title("🧠 Mental Health Resources")
st.write("Explore helpful mental health resources for single parents.")


col1, col2 = st.columns([1, 1])

with col1:
    st.components.v1.iframe("https://www.brookings.edu/articles/single-mothers-experience-high-rates-of-psychological-distress-the-safety-net-can-help/",
                            height=400,
                            scrolling=True)
    st.write("**Psychological Distress in Single Motherhood**")

with col2:
    st.components.v1.iframe("https://www.choosingtherapy.com/single-mom-depression/",
                            height=400,
                            scrolling=True)
    st.write("**Single Mom Depression: Why It Happens & How to Cope**")