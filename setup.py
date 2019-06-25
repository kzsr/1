from setuptools import setup

# https://packaging.python.org/distributing/#packaging-your-project

def readme():
    with open('README.rst') as f:
        return f.read()
setup(
    name = 'termux-apt-repo',
    version = '0.4',
    license='Apache License 2.0',
    description = 'Script to create Termux apt repositories',
    long_description = readme(),
    author = 'DWI',
    url = 'https://github.com/kzsr/1',
    scripts = ['1'],
    classifiers = (
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3'
    )
)
