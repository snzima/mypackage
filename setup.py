from setuptools import setup, find_packages

setup(
    name='awepack',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/snzima/awepack.git',
    author='Siyabonga Nzima',
    author_email='nzima822@gmail.com'
)
