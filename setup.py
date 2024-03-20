#helps in developing ml app as a package
#making it easy for distribution

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirement(file_path:str)->List[str]:

    """
    returns list of requirements
    """

    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements if req != HYPHEN_E_DOT]

    return requirements

setup(
    name= 'mlproject',
    version=' 0.0.1',
    author= 'kiitan',
    author_email= 'olaoluwaafolaranmi@gmail.com',
    packages= find_packages(),
    install_requires=get_requirement('requirements.txt')
)