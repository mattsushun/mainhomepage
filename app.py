import streamlit as st

st.title("Opioid Conversion Calculator")

# Conversion factors: per mg of drug to mg of oral morphine equivalent
CONVERSION_FACTORS = {
    ("fentanyl", "iv"): 300,  # mg fentanyl IV to mg oral morphine
    ("morphine", "po"): 1,
    ("morphine", "iv"): 3,
    ("oxycodone", "po"): 1.5,
    ("hydromorphone", "po"): 4,
    ("hydromorphone", "iv"): 20,
    ("codeine", "po"): 0.15,
    ("tramadol", "po"): 0.1,
    ("methadone", "po"): 2,
}

opioids = ["fentanyl", "morphine", "oxycodone", "hydromorphone", "codeine", "tramadol", "methadone"]
routes = {"fentanyl": ["iv"],
          "morphine": ["po", "iv"],
          "oxycodone": ["po"],
          "hydromorphone": ["po", "iv"],
          "codeine": ["po"],
          "tramadol": ["po"],
          "methadone": ["po"]}

st.sidebar.header("Current regimen")
current_opioid = st.sidebar.selectbox("Current opioid", opioids)
current_route = st.sidebar.selectbox("Route", routes[current_opioid])
current_dose = st.sidebar.number_input("Dose (mg; use mcg for fentanyl)", min_value=0.0, step=0.1)

st.sidebar.header("Convert to")
target_opioid = st.sidebar.selectbox("Target opioid", opioids)
target_route = st.sidebar.selectbox("Target route", routes[target_opioid])

if st.sidebar.button("Convert"):
    factor_from = CONVERSION_FACTORS.get((current_opioid, current_route))
    factor_to = CONVERSION_FACTORS.get((target_opioid, target_route))

    if not factor_from or not factor_to:
        st.error("Conversion factor not available for selected combination.")
    else:
        medd = current_dose * factor_from
        target_dose = medd / factor_to
        st.subheader("Results")
        st.write(f"Morphine-equivalent daily dose (MEDD): {medd:.2f} mg PO morphine")
        st.write(f"Equivalent {target_opioid} {target_route} dose: {target_dose:.2f} mg")
        st.write("Recommended start timing: Start at next scheduled dosing time.")

st.sidebar.markdown("---")
st.sidebar.write("Disclaimer: This tool provides approximate conversions using standard \
    equianalgesic ratios. Clinical judgment and patient factors must be considered.\n    Consult appropriate guidelines and a qualified healthcare professional for \n    medical decisions.")
