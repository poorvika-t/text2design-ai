import streamlit as st
import openai
import json

# ---------- CONFIG ----------
st.set_page_config(page_title="AI Text-to-Design", layout="wide")
st.title("AI-Assisted Text-to-Design Tool")
st.caption("Early-stage conceptual design | Educational use only")

st.markdown("---")

# ---------- INPUT ----------
user_input = st.text_area(
    "Describe your system in plain English",
    placeholder="Example: Water system with pump, filter, and tank",
    height=150
)

# ---------- AI FUNCTION ----------
def extract_design(text):
    prompt = f"""
You are an AI assistant for early-stage engineering design.

Allowed components:
Pump, Tank, Valve, Filter, Pipe

From the user text, extract:
1. Components used (only from allowed list)
2. Flow connections in order

Return ONLY valid JSON in this format:
{{
  "components": ["Pump", "Filter", "Tank"],
  "connections": [["Pump", "Filter"], ["Filter", "Tank"]]
}}

User text:
{text}
"""
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content

# ---------- ACTION ----------
if st.button("Generate Design"):
    if not user_input.strip():
        st.warning("Please enter a system description.")
    else:
        st.info("Analyzing input using AI...")
        result = extract_design(user_input)
        st.subheader("Structured Design Output")
        st.code(result, language="json")
