import setuptools
from setuptools.command.develop import develop
from setuptools.command.install import install
import os
import sys

with open("README.md", "r") as fh:
    long_description = fh.read()


class PostInstallCommand(install):
    """Post-installation for installation mode."""

    def run(self):
        install.run(self)
        from pyshortcuts import make_shortcut, platform
        bindir = 'bin'
        if platform.startswith('win'):
            bindir = 'Scripts'

        make_shortcut(f"{os.path.join(sys.prefix, bindir, 'pylabeler')}",
                      name='PyLabeler')


setuptools.setup(
    name="PyLabeler",
    version="0.2.0",
    author="Andrew Christiansen",
    author_email="andrewtaylorchristiansen@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/drewtchrist/pylabeler",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    include_package_data=True,
    install_requires=[
        'pyqt5',
        'pyqtwebengine',
        'qtawesome',
        'blabel',
        'qt-material',
        'qscintilla',
        'pyshortcuts'
    ],
    entry_points={
        'console_scripts': [
            'pylabeler = pylabeler.application:Application'
        ],
    },
    cmd_class={
        'install': PostInstallCommand
    }
)
