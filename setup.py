from setuptools import setup, find_packages

setup(
    name='classes',
    version='1.0.0',
    url='https://github.com/jasminemalik/FinalProject',
    author='jasminemalik',
    author_email='jm5xx@gmail.com',
    description='All classes for montecarlo simulator',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)