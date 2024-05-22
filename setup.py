from setuptools import setup, find_packages

setup(
    name='blaze_double_bot',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'undetected_chromedriver',
        'selenium',
        'requests'
    ],
    entry_points={
        'console_scripts': [
            'blaze_double_bot=blaze_double_bot.bot:main',
        ],
    },
)
``
