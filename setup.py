from setuptools import setup, find_packages

setup(
    name='givemestuff',
    version='0.4',
    author="Zhe Wang",
    author_email="wangzhetju@gmail.com",
    description="Giveme info",
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'Click',
        'requires'
    ],
    entry_points='''
        [console_scripts]
        giveme=giveme.main:cli
    ''',
)