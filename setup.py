"""
The future of web2py
"""
import subprocess
import re
from setuptools import setup


def get_version():
    regex = re.compile("__version__\s*\=\s*['\"](?P<version>.+?)['\"]")
    return regex.findall(open("py4web/__init__.py").read())[0]


setup(
    name="py4web",
    version=get_version(),
    url="https://github.com/web2py/py4web",
    license="BSD",
    author="Massimo Di Pierro",
    author_email="massimo.dipierro@gmail.com",
    maintainer="Massimo Di Pierro",
    maintainer_email="massimo.dipierro@gmail.com",
    description="Experimental py4web (a better web2py)",
    packages=["py4web", "py4web.utils", "py4web.utils.auth_plugins"],
    package_data={"py4web": ["assets/*"],},
    install_requires=[
        "bottle",
        "gunicorn",
        "gevent",
        "threadsafevariable",
        "pydal",
        "pyjwt",
        "yatl",
        "tornado",
        "pluralize",
        "requests",
    ],
    entry_points={"console_scripts": ["py4web-start=py4web.core:main"],},
    zip_safe=False,
    platforms="any",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Database :: Front-Ends",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
