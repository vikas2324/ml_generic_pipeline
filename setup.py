from setuptools import find_packages, setup
from typing import List

Hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:

  requirements=[]
  with open(file_path) as file_obj:
    requirements=file_obj.readlines()
    [req.replace("\n","")for req in requirements]
    
    if Hypen_e_dot in requirements:
       requirements.remove(Hypen_e_dot)
setup(
name='ml project',
version='0.0.1',
author='vikas sharma',
author_email='v.sharma2324@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)