import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.fhir_converter import convert_to_fhir
from backend.utils import fetch_icd11_data  # Removed fetch_data
from backend.mapping_engine import MappingEngine

app = FastAPI()

# CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Replace this with the actual path to your Excel file
DATA_FILE = rdata_file = 'C:/Users/Avhale/Downloads/NAMASTE-ICD11-FHIR/namaste-icd11-fhir/backend/data/NAMASTE_ICD11_Mapping.xlsx'
# Alternatively, use forward slashes:
# DATA_FILE = "C:/Users/Avhale/Downloads/NAMASTE-ICD11-FHIR/namaste-icd11-fhir/backend/data/NAMASTE_ICD11_Mapping.xlsx"

# Initialize the mapping engine with the combined data file
engine = MappingEngine(DATA_FILE)

@app.get("/")
def read_root():
    return {"message": "Welcome to the NAMASTE – ICD-11 Mapping & FHIR Integration API"}

@app.get("/map/{term}")
def map_term(term: str):
    """
    Maps a NAMASTE term to its corresponding ICD-11 code and display values.
    
    Args:
        term (str): The NAMASTE term to search for.
    
    Returns:
        dict: A dictionary containing NAMASTE and ICD-11 details.
    """
    mapping_details = engine.map_term_to_icd11(term)
    if mapping_details:
        return mapping_details
    return {"error": f"No mapping found for term: {term}"}

@app.post("/convert")
def convert_mapping(mapping_data: dict):
    fhir_resource = convert_to_fhir(mapping_data)
    return fhir_resource

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)