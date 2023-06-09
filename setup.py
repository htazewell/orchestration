from setuptools import setup, find_packages

setup(
    name='orchestration',
    version='1.0.7',
    description='This Python script provides functionality to schedule and execute scripts based on cron expressions. It allows executing both bash and Python scripts and provides options to add script parameters and skip conditions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Henry Tazewell',
    author_email='htazewell@gmail.com',
    url='https://github.com/htazwell/orchestration',
    packages=find_packages(),
    install_requires=[
        'croniter',
        'pytz',
    ],
)
