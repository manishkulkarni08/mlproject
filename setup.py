from setuptools import find_packages,setup
from typing import List
HYPE_E_DOT='-e .'


def get_requirements(file_path:str)->List:
    '''
    Function will return list of requirements
    '''
    requirements =[]
    with open('requirements.txt') as obj:
        requirements = obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPE_E_DOT in requirements:
            requirements.remove(HYPE_E_DOT)
    return requirements





setup(
name= 'Machine Learning Project',
version='0.0.1',
author='Manish Kulkarni',
author_email= 'manishkulkarni08@gmail.com',
packages=find_packages(),
requires=get_requirements('requirements.txt')    
)