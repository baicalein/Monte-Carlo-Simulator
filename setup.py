from setuptools import setup, find_packages

setup(
    name="MonteCarlo",                   
    version="0.1",                         
    author="Heejeong Yoon",                   
    author_email="baicalein@gmail.com",
    description="A Monte Carlo Simulator for simulating dice games and statistical analysis.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown", 
    url="https://github.com/baicalein/Monte-Carlo-Simulator.git",  
    packages=find_packages(),  
    license="MIT",
)