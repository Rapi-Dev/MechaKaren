import setuptools

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MechaKaren",
    version="1.0",
    author=["RapiDevelopment"],
    description="Free to use API Wrapper for MechaKaren API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rapi-Dev/MechaKaren.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>= 3.6',
    include_package_data=True,
    install_requires=["requests", "Colorama"]
)
