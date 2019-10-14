from setuptools import setup

setup(
    name='questions',
    version='0.0.1',
    packages=['questions'],
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=[
        'flake8>=3.6.0',
        'nose>=1.3.7',
        'slackclient==1.3.0'
    ]
)
