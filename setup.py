from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name='pgbackup',
    version='0.0.1',
    description='Database backups locally or to AWS S3',
    long_description=readme,
    author='Karolina',
    author_email='karolina.stamblewska@gmail.com',
    install_requires=[],
    packages=find_packages('src'),
    package_dir={'': 'src'},
)
