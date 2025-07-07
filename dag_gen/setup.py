from setuptools import setup, find_packages

setup(
    name='pygen',
    version='0.1.0',
    description='A Python code generator from config files',
    author='MADD',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'pygen-generator=pygen.generator:main',
        ],
    },
)
