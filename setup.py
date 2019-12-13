from distutils.core import setup

setup(
    name='surgeo',
    version='2010.1-alpha.1',
    description='Bayesian Improved Surname Geocoder model',
    long_description="""
        Surgeo is an impelmentation of the Bayesian Improved Surname 
        Geocode (BISG) model created by Mark N. Elliot et al. and 
        incluenced by the Consumer Financial Protection Bureau's (CFPB)
        implementation of the same.

    """,
    author='Theo Naunheim',
    author_email='theonaunheim@gmail.com',
    packages=[
        'surgeo',
        'surgeo.cli',
        'surgeo.models',
        'surgeo.utility',
    ],
    license='MIT',
    url='https://github.com/theonaunheim/surgeo',
    keywords=[
        'bisg',
        'disparate',
        'race'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
    ],
    requires=[
        'pandas',
        'numpy',
        'xlrd',
    ],
    package_dir={'surgeo': './surgeo'},
    package_data={'surgeo': ['./data/*']},
)
