import streamlit as st

st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)

st.set_page_config(page_title="Welcome", layout="wide")


st.markdown(
    """
    # 🐻 Welcome to BearCare!
    ## Your trusted companion for single parenthood ❤️  
    """
)

# Name Input and Enter Button
if "name" not in st.session_state:
    st.session_state.name = ""  # Initialize session state for name

# User Input
name = st.text_input("Nice to have you, what's your name?", value=st.session_state.name, key="name_input")
submit = st.button("Type your name and press Enter!")

# Display personalized message if a name is entered
if submit and name:
    st.session_state.name = name  # Store the name in session state
    st.balloons()
    st.image("https://media.giphy.com/media/xNT2CcLjhbI0U/giphy.gif?cid=ecf05e47zm553u8gtu7dq1u8y02r37bfgxe6wq4iohu0f3m2&ep=v1_gifs_related&rid=giphy.gif&ct=g")
    st.success(
        f"Welcome, {st.session_state.name}! 🎉 Nice to meet you. The navigation bar to your left shows all of the topics that this app has to offer. Feel free to peek into every page and learn more about navigating life as a single parent.")