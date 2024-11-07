import os
import pandas as pd

def load_data(file_path):
    # Ensure the file exists before attempting to read it
    if not os.path.exists(file_path):
        print(f"File {file_path} not found!")
        return None
    # Specify the engine explicitly for .xls files
    data = pd.read_excel(file_path, sheet_name=None, engine='xlrd')  # Load all sheets with xlrd engine
    return data

def main(file_path):
    data = load_data(file_path)
    if data is not None:
        print(f"Loaded data from {file_path}")
        # Your analysis code here...

# Replace with the correct path to your file
file_path = 'C:/Users/Johan/OneDrive/Desktop/Trump/downloaded_files/04c6f4f0-e1fb-4b62-bffa-1007f4c81cf3.xls'
main(file_path)
