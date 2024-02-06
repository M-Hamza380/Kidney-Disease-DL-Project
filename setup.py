"""
    It will be responsible in creating the Kidney Disease 
    Classification application as a package. You can 
    also install this package in your projects.
"""

from setuptools import setup, find_packages
from typing import List

# That function will help to install all the packages 
Hypen_E_Dot = '-e .'
def get_requirements(file_path: str) -> List[str]:

    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements ]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)
    
    return requirements



setup(
    name= 'Kidney-Disease-Classification',
    version= '0.0.1',
    author= 'M-Hamza380',
    author_email= 'hamza.anjum380@gmail.com',
    description= 'A small python package for CNN app',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)



