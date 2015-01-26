from setuptools import setup
from pip.req import parse_requirements
from pip.exceptions import InstallationError

try:
    requirements = parse_requirements("requirements.txt")
    install_requires = [str(r.req) for r in requirements]
except InstallationError:
    install_requires = []

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="github-contributors",
    version="0.0.1",
    description="github info of contributors",
    license="MIT",
    author="JuanPablo AJ",
    author_email="jpabloaj@gmail.com",
    url="https://github.com/juanpabloaj/github-contributors.git",
    packages=['github_contributors'],
    install_requires=install_requires,
    long_description=long_description,
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'github-contributors=github_contributors:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 2.7',
    ]
)
