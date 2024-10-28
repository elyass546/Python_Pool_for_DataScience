import pandas as pd
from typing import Optional

def load(path: str) -> Optional[pd.DataFrame]:
    try:
        # Load the dataset
        dataset = pd.read_csv(path)
        
        # Write (print) the dimensions of the dataset
        print(f"Loading dataset of dimensions {dataset.shape}")
        
        # Return the dataset
        return dataset
    
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
        return None
    except pd.errors.ParserError:
        print("Error: File is not in a valid CSV format.")
        return None
