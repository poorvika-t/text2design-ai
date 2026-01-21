import streamlit as st

st.set_page_config(page_title="AI Text-to-Design", layout="wide")

st.title("AI-Assisted Text-to-Design Tool")
st.caption("Early-stage conceptual design | Educational use only")

st.markdown("---")

user_input = st.text_area(
    "Describe your system in plain English",
    placeholder="Example: Water system with pump, filter, and tank",
    height=150
)

if st.button("Generate Design"):
    st.info("Processing your input...")
