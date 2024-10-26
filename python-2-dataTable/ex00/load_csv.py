import pandas as pd

def main():
    load("life_expectancy_years.csv")
    return

def load(path: str) -> None: # (You have to adapt the type of return according to your library)
    # I should check if the path correct before reading it
    df = pd.read_csv(path)
    print(df)

if __name__ == "__main__":
    main()