from setuptools import setup, find_packages

setup(
    name='chromote',
    version='0.4.0',
    description="Python Wrapper for the Google Chrome Remote Debugging Protocol",
    author='Chris Seymour',
    packages=find_packages(),
    install_requires=['requests', 'websocket-client']
)
