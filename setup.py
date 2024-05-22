from setuptools import setup, find_packages
with open('README.md, 'r') as f:
          readme =f.read()

setup(
    name='blaze_double_bot',
    version='0.1.0',
    author='Rafael de Oliveira Ribeiro',
    long_description=readme,
    long_description_content_type='text/markdown',
    author_email='ror74559@gmail.com',
    description='This Python script automates the betting process on the Blaze Double',
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
