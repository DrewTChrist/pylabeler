import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="PyLabeler",
    version="0.1.0",
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
        'qt-material'
        'qscintilla'
    ],
    entry_points={
        'console_scripts': [
             'pylabeler = pylabeler.application:Application'
        ],
    },
)
