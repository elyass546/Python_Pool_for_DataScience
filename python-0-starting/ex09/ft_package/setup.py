from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    description="A sample test package",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="ie-laabb",
    author_email=" ie-laabb@student.1337.ma",
    url="https://github.com/elyass546/ft_package",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)