from setuptools import setup, find_packages

setup(
    version='1.0.0',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    name='src',
    packages=find_packages('src'),
    package_dir={'': 'src'},
)