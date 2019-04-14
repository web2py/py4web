"""
"""

from setuptools import setup

setup(
    name='web3py',
    version='0.1.0',
    url='https://github.com/web2py/web3py',
    license='BSD',
    author='Massimo Di Pierro',
    author_email='massimo.dipierro@gmail.com',
    maintainer='Massimo Di Pierro',
    maintainer_email='massimo.dipierro@gmail.com',
    description='Expeerimental web3py (a better web2py)',
    long_description=__doc__,
    packages=['web3py'],
    include_package_data=True,
    install_requires=[
        'bottle',
        'gunicorn',
        'gevent'
        'reloader'
        'pydal',
        'yatl',
        ],
    entry_points = {
        'console_scripts': ['web2py-start=web2py.core:main'],
        }
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
