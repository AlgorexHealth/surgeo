#from distutils.core import setup
from cx_Freeze import setup
from cx_Freeze import Executable

# cx_Freeze option
BASE = 'Win32GUI'

setup(
    # cx_Freeze setup.py
    executables=[Executable("./surgeo/app/common_entry.py", base=BASE)],
    target_name='surgeo',
    add_to_path=True,
    install_icon='./static/logo.gif',
    # Normal setup.py
    name='surgeo',
    version='1.0.1',
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
        'surgeo.app',
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
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
    ],
    requires=[
        'pandas',
        'numpy',
        'xlrd',
    ],
    package_dir={'surgeo': './surgeo'},
    package_data={'surgeo': ['./data/*', './static/*']},
)