  
from setuptools import setup

with open("README.md", "r", encoding="utf-8", errors="ignore") as fh:
    readme = fh.read()

setup(name='MechaKaren.py',
      author=['Daftscientist', 'S4qib'],
      url='https://github.com/Rapi-Dev/MechaKaren.py/',
      version='1.0',
      packages=['MechaKaren'],
      license='MIT',
      description='A Python wrapper for the MechaKaren API',
      long_description=readme,
      long_description_content_type="text/x-rst",
      include_package_data=True,
      install_requires=['requests', 'Colorama'],
      python_requires='>=3.8.0',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
      ]
)
