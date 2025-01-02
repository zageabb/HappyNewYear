import streamlit as st

# Title of the app (optional)
st.title("Dancing Santa 🎅")

# Embed the GIF
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://raw.githubusercontent.com/zageabb/XmasTimer/refs/heads/main/happy-christmas-dancing-santa.gif" alt="Dancing Santa" style="width: 100%; max-width: 600px;">
    </div>
    """,
    unsafe_allow_html=True,
)
