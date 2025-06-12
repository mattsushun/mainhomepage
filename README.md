# Opioid Converter

This repository contains a simple Streamlit web application for converting between common opioids using approximate equianalgesic ratios.

## Features
- Convert a current opioid dose to a morphine-equivalent daily dose (MEDD).
- Convert MEDD to an equivalent dose of another opioid and route.
- Displays a recommended start timing for the target medication.

## Usage
Install the required dependencies and run the app with Streamlit:

```bash
pip install streamlit
streamlit run app.py
```

The sidebar widgets allow selection of the current opioid, route, and dose, as well as the desired target opioid and route. Press **Convert** to see the results.

> **Disclaimer:** This tool provides approximate conversions based on standard equianalgesic ratios. It is not a substitute for professional medical judgment. Always consult appropriate guidelines and a qualified healthcare professional when adjusting opioid therapy.
