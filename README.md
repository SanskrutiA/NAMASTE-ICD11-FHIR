#  NAMASTE – ICD-11 Mapping & FHIR Integration  

##  Overview  
This project demonstrates the integration of **AYUSH NAMASTE Terminologies** with **WHO ICD-11 clinical entities**, generating a **FHIR-compliant ProblemList** for interoperability.  

It provides:  
- A **mapping engine** that connects local NAMASTE terms (like *Vibandha*) to ICD-11 codes (e.g., *ME05.0 Constipation*).  
- A **FHIR Converter** that transforms mappings into valid FHIR resources (e.g., `Condition` / `ProblemListEntry`).  
- An **API workflow** to fetch and merge terminology data from WHO ICD-11 APIs and local NAMASTE datasets.  

---

#  Workflow  

### Example: Vibandha → Constipation  

1. **Input**: User enters term *Vibandha*  
2. **API Search**: Query WHO ICD-11 API → finds *ME05.0 Constipation*  
3. **Mapping Engine**: Links NAMASTE term with ICD-11 concept → generates ConceptMap  
4. **FHIR Converter**: Produces FHIR-compliant `ProblemListEntry`  

---

## 🛠️ Tech Stack  

###  Backend  
- **Python 3.10+**  
- **FastAPI** → REST APIs  
- **Pandas** → Handle NAMASTE CSV/Excel  
- **Requests / HTTPx** → ICD-11 API calls  
- **fhir.resources** → FHIR model classes  

###  Frontend (Optional)  
- **React + TailwindCSS** → Web UI  
- **FHIR Viewer Components** (optional)  

###  Data  
- **NAMASTE CSV/Excel file** (provided)  
- **WHO ICD-11 API** → [https://icd.who.int/icdapi](https://icd.who.int/icdapi)  

###  Deployment  
- **Docker** (containerization)  
- **GitHub Actions** (CI/CD optional)  
- **Render / Railway / GCP / AWS**  

---

##  Project Structure  
namaste-icd11-fhir/
│── backend/
│ ├── main.py # FastAPI entry
│ ├── mapping_engine.py # Logic for NAMASTE ↔ ICD-11
│ ├── fhir_converter.py # Convert mapping → FHIR resources
│ ├── utils.py # Helpers (API calls, CSV parsing)
│ └── data/
│ └── NAMASTE_ICD11_Mapping.xlsx
│
│── frontend/ (optional)
│ ├── src/
│ ├── package.json
│ └── ...
│
│── tests/
│ ├── test_mapping.py
│ └── test_fhir.py
│
│── README.md
│── requirements.txt
│── docker-compose.yml
│── .gitignore
