from setuptools import setup

setup(
    name='pypass',
    version='0.0.1',
    author='',
    py_modules=['pypass'],
    install_requires=['Click',
                      'requests'],
    entry_points='''
        [console_scripts]
        pypass=pypass:pypass
    ''',
)
