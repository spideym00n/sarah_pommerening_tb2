import streamlit as st
from utils.mongo import add_message, get_all_messages

# Page Configuration

st.logo(
    "https://cdn-icons-png.flaticon.com/512/9029/9029906.png",
    size="large",
    icon_image="https://cdn-icons-png.flaticon.com/512/1256/1256449.png",
)


st.title("Advice & Motivation Board🖤")
st.write("Share your advice, experiences, or a few kind words to motivate others!")

# Input Section
st.subheader("💬 Leave a Message")
username = st.text_input("Your Name (Optional):", placeholder="Anonymous")
message = st.text_area("Your Message:", placeholder="Share your advice or motivation here...")

if st.button("Submit Message"):
    if message.strip() != "":
        add_message(username or "Anonymous", message)
        st.success("Thank you for sharing! Your message has been posted.")
    else:
        st.warning("Please write something before submitting.")

st.write("---")

# Display Messages
st.subheader("📝 Community Messages")

messages = get_all_messages()
if messages:
    for msg in messages:
        st.write(f"**{msg['username']}** wrote:")
        st.info(msg['message'])
        st.caption(f"🕒 {msg['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
        st.write("---")
else:
    st.write("No messages yet. Be the first to leave one!")
