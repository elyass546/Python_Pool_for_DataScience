import pandas as pd
from typing import Optional

def main():
    data = load("life_expectancy_years.csv")
    print(data)

def load(path: str) -> Optional[pd.DataFrame]:
    try:
        # Load the dataset
        dataset = pd.read_csv(path)

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

if __name__ == "__main__":
    main()