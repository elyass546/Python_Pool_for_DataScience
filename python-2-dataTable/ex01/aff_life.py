import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt


def main():
    display_country_informations("../ex00/life_expectancy_years.csv")


def display_country_informations(path: str):
    try:
        dataset = load(path)

        country_data = dataset[dataset['country'] == 'Morocco']
        if country_data.empty:
            print("No data found for the chosen country")
            return

        # Reshape data for plotting
        country_data = country_data.drop(columns='country').T
        country_data.columns = ['Life Expectancy']
        country_data.index.name = 'Year'
        country_data.reset_index(inplace=True)

        # Convert 'Year' and 'Life Expectancy' columns to appropriate types
        country_data['Year'] = country_data['Year'].astype(int)
        life_expectancy_year = country_data['Life Expectancy'].astype(float)

        # Convert columns to numpy arrays and ensure they are 1D
        years = country_data['Year'].to_numpy().reshape(-1)
        life_expectancy = life_expectancy_year.to_numpy().reshape(-1)

        # Plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(x=years, y=life_expectancy)
        plt.title("Life Expectancy in Morocco Over Time")
        plt.xlabel("Year")
        plt.ylabel("Life Expectancy")
        plt.xticks(rotation=45)

        # Display years every 40 years on the x-axis
        start_year = country_data['Year'].min()
        end_year = country_data['Year'].max()
        plt.xticks(range(start_year, end_year + 1, 40), rotation=45)

        plt.show()

    except KeyError as e:
        print(f"Error: Missing expected column - {e}")


if __name__ == "__main__":
    main()
