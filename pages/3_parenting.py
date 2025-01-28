import streamlit as st
import webbrowser


st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


st.set_page_config(page_title="Parenting", layout="wide")

st.title("Videos on parenting")
st.write("As a single parent, the reality of parenting is much different for you, than it might be for others, which these videos specifically on that topic might be interesting to you!")

video_url1 = "https://youtu.be/RDemM6FjcSE?si=STfdK97OzPsUmRBa"
video_url2= "https://youtu.be/PHJfP1Q4tYo?si=wg5IIHBk3gwoblXH"
video_url3= "https://youtu.be/sbKdETsy90c?si=SwBeWHsWGgKFRktS"

col1, col2, col3 = st.columns([1, 1, 1])


with col1:
    st.video(video_url1)
    st.write("**6:10min:** Parenting Tips for Single Parents")

with col2:
    st.video(video_url2)
    st.write("**19:44min:** Balancing Work and Parenting")

with col3:
    st.video(video_url3)
    st.write("**1:01min:** Emotional Support for Single Parents")