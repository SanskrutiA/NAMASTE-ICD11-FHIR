from fhir.resources.condition import Condition

def create_condition_resource(namaste_term, icd_code, description):
    condition = Condition(
        resourceType="Condition",
        id=icd_code,
        code={
            "coding": [
                {
                    "system": "http://hl7.org/fhir/sid/icd-11",
                    "code": icd_code,
                    "display": description
                }
            ],
            "text": f"{namaste_term} mapped to {description}"
        },
        clinicalStatus={"coding": [{"system": "http://terminology.hl7.org/CodeSystem/condition-clinical", "code": "active"}]},
        subject={"reference": "Patient/example"},  # Placeholder for patient reference
        onsetDateTime="2023-01-01T00:00:00Z"  # Placeholder for onset date
    )
    return condition

def convert_to_fhir(mapping_data):
    """
    Converts mapping data into FHIR Condition resources.
    
    Args:
        mapping_data (dict): A dictionary containing NAMASTE term, ICD-11 code, and description.
    
    Returns:
        list: A list of FHIR Condition resources.
    """
    fhir_resources = []
    for entry in mapping_data:
        namaste_term = entry.get('NAMASTE_Term')
        icd_code = entry.get('ICD11_Code')
        description = entry.get('Description', 'No description provided')
        condition = create_condition_resource(namaste_term, icd_code, description)
        fhir_resources.append(condition.dict())
    return fhir_resources