import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Text-to-Design", layout="wide")

st.title("AI-Assisted Text-to-Design Tool")
st.caption("Prototype for Generative Engineering Design")
st.warning("⚠️ Conceptual output only. Final designs must be validated by certified engineers.")

st.markdown("---")

# ---------------- INPUT ----------------
user_input = st.text_area(
    "Describe your system in plain English",
    placeholder="Example: Water system with pump, filter and tank",
    height=150
)

# ---------------- MOCK AI PARSER ----------------
def mock_ai_parser(text):
    text = text.lower()

    components = []
    if "pump" in text:
        components.append("Pump")
    if "filter" in text:
        components.append("Filter")
    if "tank" in text:
        components.append("Tank")
    if "valve" in text:
        components.append("Valve")

    connections = []
    for i in range(len(components) - 1):
        connections.append([components[i], components[i + 1]])

    return {
        "components": components,
        "connections": connections
    }

# ---------------- RULE VALIDATION ----------------
def validate_design(data):
    warnings = []

    if len(data["components"]) < 2:
        warnings.append("System should contain at least two components.")

    if not data["connections"]:
        warnings.append("No flow connections detected between components.")

    return warnings

# ---------------- FLOW DIAGRAM (NO EXTRA LIBS) ----------------
def draw_flow(design):
    comps = design["components"]

    if not comps:
        st.info("No components available to visualize.")
        return

    html = "<div style='display:flex; align-items:center; justify-content:center;'>"

    for i, comp in enumerate(comps):
        html += f"""
        <div style="
            border:2px solid #4CAF50;
            padding:20px;
            min-width:120px;
            text-align:center;
            border-radius:10px;
            font-weight:bold;
            background-color:#F9FFF9;
            ">
            {comp}
        </div>
        """

        if i < len(comps) - 1:
            html += "<div style='font-size:30px; margin:0 15px;'>➡️</div>"

    html += "</div>"

    st.markdown(html, unsafe_allow_html=True)


# ---------------- EXPLANATION PANEL ----------------
def explain_design(design):
    explanation = []

    if "Pump" in design["components"]:
        explanation.append("Pump initiates flow and maintains required pressure.")

    if "Filter" in design["components"]:
        explanation.append("Filter removes impurities to protect downstream components.")

    if "Tank" in design["components"]:
        explanation.append("Tank provides storage and balances demand fluctuations.")

    if not explanation:
        explanation.append("Basic system detected. Add more components for better functionality.")

    return explanation

# ---------------- MAIN ACTION ----------------
if st.button("Generate Design"):
    if not user_input.strip():
        st.warning("Please enter a system description.")
    else:
        st.success("Input processed successfully")

        design = mock_ai_parser(user_input)
        warnings = validate_design(design)

        st.subheader("Structured Design Output")
        st.json(design)

        st.subheader("System Flow Diagram")
        draw_flow(design)

        st.subheader("Design Explanation")
        for line in explain_design(design):
            st.write("•", line)

        if warnings:
            st.subheader("Validation Warnings")
            for w in warnings:
                st.warning(w)
        else:
            st.success("Design passed basic validation checks.")

        st.markdown("---")
        st.caption(
            "Note: AI logic is simulated for prototype demonstration. "
            "In real-world deployment, this module would be powered by a trained LLM "
            "and integrated with CAD/BIM tools."
        )
