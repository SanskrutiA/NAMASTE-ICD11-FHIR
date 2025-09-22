# utils.py

import pandas as pd

def fetch_icd11_data(file_path):
    """
    Reads ICD-11 data from an Excel file.
    
    Args:
        file_path (str): Path to the Excel file containing ICD-11 data.
    
    Returns:
        list: A list of dictionaries representing the ICD-11 data.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')

def read_namaste_data(file_path):
    return pd.read_excel(file_path)

def parse_mapping_data(mapping_data):
    # Implement parsing logic here
    parsed_data = {}
    for item in mapping_data:
        # Example parsing logic
        term = item['NAMASTE_Term']
        code = item['ICD11_Code']
        parsed_data[term] = code
    return parsed_data

def save_to_excel(data, output_file):
    df = pd.DataFrame(data.items(), columns=['NAMASTE_Term', 'ICD11_Code'])
    df.to_excel(output_file, index=False)

def fetch_combined_data(file_path):
    """
    Reads combined NAMASTE and ICD-11 data from a single Excel file.
    
    Args:
        file_path (str): Path to the Excel file containing the data.
    
    Returns:
        list: A list of dictionaries representing the combined data.
    """
    df = pd.read_excel(file_path)
    return df.to_dict(orient='records')