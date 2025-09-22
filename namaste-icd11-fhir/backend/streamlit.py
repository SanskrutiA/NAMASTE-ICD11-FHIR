import streamlit as st
import requests

# Base URL of your FastAPI backend
BASE_URL = "http://localhost:8000"

st.set_page_config(page_title="NAMASTE – ICD-11 Mapping", layout="wide")

st.title("🩺 NAMASTE – ICD-11 Mapping & FHIR Converter")

# ---- Term Mapping ----
st.header("🔍 Search NAMASTE → ICD-11 Mapping")

term = st.text_input("Enter a NAMASTE term:")

if st.button("Map Term"):
    if term.strip():
        response = requests.get(f"{BASE_URL}/map/{term}")
        if response.status_code == 200:
            result = response.json()
            if "error" in result:
                st.error(result["error"])
            else:
                st.success("✅ Mapping Found")
                st.json(result)
        else:
            st.error("⚠️ Failed to fetch mapping. Check backend server.")
    else:
        st.warning("Please enter a term to map.")

# ---- FHIR Conversion ----
st.header("🧩 Convert Mapping → FHIR Resource")

mapping_data = st.text_area(
    "Paste NAMASTE → ICD-11 mapping data (JSON format):", 
    height=200,
    placeholder='{"namaste_term": "Example", "icd11_code": "XX.YY", "display": "Example disease"}'
)

if st.button("Convert to FHIR"):
    try:
        if mapping_data.strip():
            import json
            data = json.loads(mapping_data)
            response = requests.post(f"{BASE_URL}/convert", json=data)
            if response.status_code == 200:
                st.success("✅ FHIR Resource Generated")
                st.json(response.json())
            else:
                st.error(f"⚠️ Error: {response.text}")
        else:
            st.warning("Please provide mapping data in JSON format.")
    except Exception as e:
        st.error(f"Invalid JSON: {e}")

# ---- Root Endpoint ----
if st.sidebar.button("Check Backend Status"):
    response = requests.get(BASE_URL + "/")
    if response.status_code == 200:
        st.sidebar.success(response.json()["message"])
    else:
        st.sidebar.error("Backend not reachable 🚨")
