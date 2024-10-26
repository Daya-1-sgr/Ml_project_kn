from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    '''this function will return a list of all the requirements'''
    requirements=[]
    hypen_e_comma='-e .'
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        if hypen_e_comma in requirements:
            requirements.remove(hypen_e_comma)
    return requirements

setup(
    name='MLProject1',
    version='0.0.1',
    author='Dayaban Sagar',
    author_email='dayabansgr@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)