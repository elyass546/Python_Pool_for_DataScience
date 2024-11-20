import seaborn as sns
from load_csv import load
import matplotlib.pyplot as plt


def main():
    life_expectancy_years = load("../ex00/life_expectancy_years.csv")
    income_per_person = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    if life_expectancy_years is not None and income_per_person is not None:
        project_Life_Expectancy_GNP_1900(
            life_expectancy_years, income_per_person)


# displays the projection of life expectancy
# in relation to the gross national product of
# the year 1900 for each country.
def project_Life_Expectancy_GNP_1900(life_expectancy_years, income_per_person):
    # Extracting the relevant columns
    life_expectancy_1900 = life_expectancy_years['1900']
    gnp_1900 = income_per_person['1900']  # Adjust the column name as necessary

    # Creating a scatter plot
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=gnp_1900, y=life_expectancy_1900, color='blue', s=100)

    # Adding titles and labels
    plt.title('1900')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')

    # Set a logarithmic scale for the x-axis and customize ticks
    plt.xscale('log')
    plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])

    # Show grid
    plt.grid(False)

    # Display the plot
    plt.show()


if __name__ == "__main__":
    main()
