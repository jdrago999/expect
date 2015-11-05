from distutils.core import setup

setup(
    name='expect',
    version='0.1.0',
    author='Foo Barley',
    author_email='foo@example.com',
    packages=['expect', 'expect.tests'],
    url='https://github.com/sumeet/expect',
    description='Mocks and stubs for Python with RSpec\'s syntax',
    long_description=open('README.markdown').read(),
    install_requires=[
        'exam==0.8.0',
        'expecter==0.2.2',
        'mock==1.0.1',
        'nose==1.1.2',
        'spec==0.9.7',
        'wsgiref==0.1.2',
    ],
)