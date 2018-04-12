from setuptools import setup, find_packages

setup(
    name='jsviewer',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['jsviewer'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        jsviewer = app.cli.main:cli
        jsv = app.cli.main_cli:cli
    ''',
)
