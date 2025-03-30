import streamlit as st

st.title("📝 Occupational Therapy Note Generator")

# Define intervention templates
interventions = {
    "ADLs": "Patient participated in ADL training focusing on {details}. OT provided verbal cues and assistance to improve independence and safety.",
    "Upper Extremity Exercises": "Patient completed upper extremity exercises using {details}. OT monitored form and provided cues to optimize technique.",
    "Balance Training": "Patient performed balance activities such as {details}. OT provided assistance and safety monitoring throughout.",
    "Functional Mobility": "Patient practiced functional mobility tasks including {details}. OT provided cues for safe technique and posture.",
    "Safety Education": "OT provided safety education including {details}. Patient was instructed on precautions to reduce fall risk."
}

# --- Input Form ---
with st.form("ot_note_form"):
    intervention_type = st.selectbox("Select Intervention", list(interventions.keys()))
    details = st.text_input(f"Enter details for {intervention_type.lower()} (e.g., toileting, 2 lb handweights)")
    assistance_level = st.selectbox("Assistance Level", ["Independent", "SBA", "CGA", "Min assist", "Mod assist", "Max assist", "Dependent"])
    submit = st.form_submit_button("Generate Note")

# --- Note Generation ---
if submit:
    intervention_text = interventions[intervention_type].format(details=details)

    note = f"""
{intervention_text} Assistance level required: {assistance_level}.
"""
    st.markdown("### 🧾 Generated OT Note")
    st.text(note)

