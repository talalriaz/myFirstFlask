from setuptools import setup, find_packages


setup(
    author="Talal",
    description="A very basic Flask implementation",
    name="myFirstFlask",
    version="0.1.0",
    packages=find_packages(include=('myFirstFlask', 'myFirstFlask.*')),
    install_requires=['flask>=2.2.0'],
    python_requires='>=3.7.*',
)
