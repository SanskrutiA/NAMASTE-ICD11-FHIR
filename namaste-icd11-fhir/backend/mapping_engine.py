from backend.utils import fetch_combined_data

class MappingEngine:
    def __init__(self, data_file):
        self.data = fetch_combined_data(data_file)

    def map_term_to_icd11(self, term):
        """
        Maps a local NAMASTE term to its corresponding ICD-11 code and display values.
        
        Args:
            term (str): The NAMASTE term to map.
        
        Returns:
            dict: A dictionary containing NAMASTE and ICD-11 details, or None if not found.
        """
        for entry in self.data:
            if entry['NAMASTE_Display'] == term:
                return {
                    "NAMASTE_Code": entry['NAMASTE_Code'],
                    "NAMASTE_Display": entry['NAMASTE_Display'],
                    "ICD11_Code": entry['ICD11_Code'],
                    "ICD11_Display": entry['ICD11_Display']
                }
        return None

    def generate_concept_map(self):
        """
        Generates a ConceptMap linking NAMASTE terms to ICD-11 codes.
        
        Returns:
            list: A list of mappings between NAMASTE terms and ICD-11 codes.
        """
        concept_map = []
        for entry in self.data:
            concept_map.append({
                'namaste_term': entry['NAMASTE_Term'],
                'icd11_code': entry['ICD11_Code']
            })
        return concept_map

# Example usage (to be removed in production)
if __name__ == "__main__":
    data_file = data_file = 'C:/Users/Avhale/Downloads/NAMASTE-ICD11-FHIR/namaste-icd11-fhir/backend/data/NAMASTE_ICD11_Mapping.xlsx'

    engine = MappingEngine(data_file)
    print(engine.map_term_to_icd11('Vibandha'))
    print(engine.generate_concept_map())