from setuptools import setup, find_packages

install_requires = ["pytest", "PyYAML", "tornado"]

setup(
    name='swarm-af-server',
    description='A cool swarm project, yo',
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True)
