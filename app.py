import streamlit as st
import json



# ---------- CONFIG ----------
st.set_page_config(page_title="AI Text-to-Design", layout="wide")

st.title("AI-Assisted Text-to-Design Tool")
st.caption("Early-stage conceptual design | Educational use only")
st.warning("⚠️ Conceptual schematic only. Final validation by a qualified engineer is required.")

st.markdown("---")

# ---------- INPUT ----------
user_input = st.text_area(
    "Describe your system in plain English",
    placeholder="Example: Water system with pump, filter, and tank",
    height=150
)

# ---------- MOCK AI FUNCTION ----------
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
def draw_flow(design):
    comps = design["components"]

    if not comps:
        st.info("No components to visualize.")
        return

    cols = st.columns(len(comps))

    for i, comp in enumerate(comps):
        with cols[i]:
            st.markdown(
                f"""
                <div style="
                    border:2px solid #4CAF50;
                    padding:20px;
                    text-align:center;
                    border-radius:10px;
                    font-weight:bold;">
                    {comp}
                </div>
                """,
                unsafe_allow_html=True
            )

        if i < len(comps) - 1:
            st.markdown("<h2 style='text-align:center;'>➡️</h2>", unsafe_allow_html=True)

# ---------- RULE VALIDATION ----------
def validate_design(data):
    warnings = []

    if len(data["components"]) < 2:
        warnings.append("System should have at least two connected components.")

    if len(data["connections"]) == 0:
        warnings.append("No valid flow connections detected.")

    return warnings

# ---------- ACTION ----------
if st.button("Generate Design"):
    if not user_input.strip():
        st.warning("Please enter a system description.")
    else:
        st.info("Analyzing input (AI-assisted logic)...")

        design = mock_ai_parser(user_input)
        warnings = validate_design(design)

        st.subheader("Structured Design Output")
        st.json(design)
        st.subheader("System Flow Diagram")
        diagram = generate_diagram(design)
        st.graphviz_chart(diagram)


        if warnings:
            st.subheader("Validation Warnings")
            for w in warnings:
                st.warning(w)
        else:
            st.success("Design passed basic validation checks.")

        st.markdown("---")
        st.caption("Note: AI logic simulated for prototype demonstration.")
        st.subheader("System Flow Diagram")
        draw_flow(design)

def generate_diagram(design):
     dot = Digraph()

     for comp in design["components"]:
        dot.node(comp, comp)

     for conn in design["connections"]:
        dot.edge(conn[0], conn[1])

     return dot
def explain_design(design):
     explanation = []

     if "Pump" in design["components"]:
        explanation.append("Pump initiates flow and maintains pressure.")

     if "Filter" in design["components"]:
        explanation.append("Filter removes impurities before storage or distribution.")

     if "Tank" in design["components"]:
        explanation.append("Tank provides storage and balances demand fluctuations.")

     return explanation
st.subheader("Design Explanation")
for line in explain_design(design):
    st.write("•", line)


