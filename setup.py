from setuptools import setup

setup(

    name="cli-calculator",
    version="0.1",
    packages=['calculator','tests'],
    install_requirements=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    calc=calculator.cli:calc
    '''
)

