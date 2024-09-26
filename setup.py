# setup.py
from setuptools import setup, find_packages

setup(
    name='trading_backtester',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        # List your dependencies here
        'pandas',
        'numpy',
        'matplotlib',
        'yfinance',
        # Add other dependencies as needed
    ],
    author='watrgoat',
    author_email='olivermatthew601@gmail.com',
    description='A Python backtesting library for algorithmic trading strategies.',
    url='https://github.com/yourusername/trading-backtester',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11, <4',
)
