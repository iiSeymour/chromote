from setuptools import setup, find_packages

setup(
    name='chromote',
    version='0.1.2',
    description="Python Wrapper for the Google Chrome Remote Debugging Protocol",
    author='Chris Seymour',
    packages=find_packages(),
    install_requires=['requests', 'ws4py']
)
