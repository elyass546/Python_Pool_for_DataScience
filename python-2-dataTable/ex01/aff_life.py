# Import seaborn
import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt

def main():
    display_country_informations("../ex00/life_expectancy_years.csv")
    return

def display_country_informations(path: str):
    try:
        dataset = load(path)
        
        country_data = dataset[dataset['country'] == 'Morocco']
        if country_data.empty:
            print(f"No data found for the chosen country")
            return

        # Reshape data for plotting
        # We drop the 'country' column and set years as the columns
        country_data = country_data.drop(columns='country').T
        country_data.columns = ['Life Expectancy']
        country_data.index.name = 'Year'
        country_data.reset_index(inplace=True)

        # Convert the 'Year' column to integers if needed
        country_data['Year'] = country_data['Year'].astype(int)

        # Plot the data
        plt.figure(figsize=(10, 6))
        sns.lineplot(data=country_data, x='Year', y='Life Expectancy')
        plt.title(f"Life Expectancy in Morocco Over Time")
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