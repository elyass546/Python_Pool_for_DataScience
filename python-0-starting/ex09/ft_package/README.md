
This is a sample Python package created for Exercise 09 in Python_00. It contains a function `count_in_list` that counts occurrences of an item in a list.

# Create the source distribution and wheel distribution
python3 setup.py sdist bdist_wheel

# Now that the package is built, you can install it locally using pip:
pip install ./dist/ft_package-0.0.1-py3-none-any.whl

# Verify that the package is installed:
pip show -v ft_package