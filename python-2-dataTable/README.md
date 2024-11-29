# Training Piscine Python for Datascience - Day 02

Welcome to the *Day 02* exercises of the Python training piscine. This repository focuses on loading, manipulating, and visualizing datasets using Python.

## Table of Contents

1. [General Rules](#general-rules)
2. [Specific Instructions of the Day](#specific-instructions-of-the-day)
3. [Exercises](#exercises)
   - [Exercise 00: Load my Dataset](#exercise-00-load-my-dataset)
   - [Exercise 01: Draw my Country](#exercise-01-draw-my-country)
   - [Exercise 02: Compare my Country](#exercise-02-compare-my-country)
   - [Exercise 03: Draw my Year](#exercise-03-draw-my-year)
4. [Submission Guidelines](#submission-guidelines)

---

## General Rules

- Use *Python 3.10* for all exercises.
- Avoid using global variables.
- Follow Python best practices for imports, naming conventions, and file organization.
- Each script must have a main() function and a __doc__ string for documentation.
- Use flake8 for linting (pip install flake8).
- Test your code thoroughly before submission.

---

## Specific Instructions of the Day

- No code should exist in the global scope; everything must be inside functions.
- Use Python libraries such as pandas, matplotlib, and seaborn for dataset manipulation and visualization.
- Handle errors gracefully and display clear error messages.
- Use data from *Gapminder.org* (CC-BY License) for exercises.

---

## Exercises

### Exercise 00: Load my Dataset
- *Directory*: ex00/
- *File*: load_csv.py
- *Goal*: Implement a function that loads a CSV file, displays its dimensions, and returns the dataset.

---

### Exercise 01: Draw my Country
- *Directory*: ex01/
- *Files*: load_csv.py, aff_life.py
- *Goal*: Create a visualization of life expectancy data for your campus's country using life_expectancy_years.csv.

---

### Exercise 02: Compare my Country
- *Directory*: ex02/
- *Files*: load_csv.py, aff_pop.py
- *Goal*: Compare population data of your campus's country with another country using population_total.csv for the years 1800 to 2050.

---

### Exercise 03: Draw my Year
- *Directory*: ex03/
- *Files*: load_csv.py, projection_life.py
- *Goal*: Visualize the correlation between life expectancy and GDP per capita for the year 1900 using income_per_person_gdppercapita_ppp_inflation_adjusted.csv and life_expectancy_years.csv.

---

## Submission Guidelines

- Submit your work in the assigned Git repository. Only files in the repository will be graded.
- Ensure all files are named correctly and placed in their respective directories.
- Test your solutions with peers for better feedback.

---

## License

This project is licensed under the MIT License.