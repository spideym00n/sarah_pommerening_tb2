import streamlit as st


st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


st.set_page_config(page_title="Finances", layout="wide")

st.title("Finances")
st.write("What's better than saving time AND money?")
col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    st.components.v1.iframe("https://www.singlemothersurvivalguide.com/",
                            height=400,
                            scrolling=True)
with col2:
    st.components.v1.iframe("https://www.ellevest.com/magazine/personal-finance/single-moms",
                            height=400,
                            scrolling=True)
with col3:
    st.components.v1.iframe("https://www.members1st.org/blog/articles/budgeting-tips-for-single-parents/",
                            height=400,
                            scrolling=True)