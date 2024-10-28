import seaborn as sns
from load_csv import load
import pandas as pd
import matplotlib.pyplot as plt

def main():
    # Usage example:
    plot_population_two_countries("population_total.csv", "Morocco", "France")
    return

def preprocess_population_data(dataset, country):
    # Filter for the selected country and reshape
    country_data = dataset[dataset['country'] == country]
    if country_data.empty:
        print(f"No data found for country: {country}")
        return None
    
    # Transpose and clean data
    country_data = country_data.drop(columns='country').T
    country_data.columns = ['Population']
    country_data.index.name = 'Year'
    country_data.reset_index(inplace=True)

    # Convert "Population" column to numeric (strip 'M' and convert to float)
    country_data['Population'] = country_data['Population'].str.replace('M', '').astype(float)
    return country_data

def plot_population_two_countries(file_path, country1, country2):
    # Load and preprocess the dataset
    dataset = load(file_path)
    if dataset is None:
        return
    
    data_country1 = preprocess_population_data(dataset, country1)
    data_country2 = preprocess_population_data(dataset, country2)
    
    if data_country1 is None or data_country2 is None:
        return
    
    # Add a column to identify each country
    data_country1['Country'] = country1
    data_country2['Country'] = country2

    # Concatenate data for both countries
    combined_data = pd.concat([data_country1, data_country2])

    # Convert the 'Year' column to integers if needed
    combined_data['Year'] = combined_data['Year'].astype(int)

    # Plot the data
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=combined_data, x='Year', y='Population', hue='Country')
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population (in millions)")

    # Set x-axis ticks every 40 years, up to 2050
    start_year = combined_data['Year'].min()
    end_year = min(combined_data['Year'].max(), 2050)  # Limit to 2050
    plt.xticks(range(start_year, end_year + 1, 40), rotation=45)

    # Set y-axis ticks in increments of 20M
    y_max = combined_data['Population'].max()
    plt.yticks(range(0, int(y_max) + 1, 20), labels=[f"{y}M" for y in range(0, int(y_max) + 1, 20)])

    plt.legend(title='Country')
    plt.show()


if __name__ == "__main__":
    main()