from setuptools import find_packages, setup

with open("./src/README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='enigma',
    packages=find_packages(include=['enigma']),
    version='0.1.0',
    description='Enigma machine simulator',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Rodrigo de Souza',
    author_email='rsouza01@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.2.1'],
    test_suite='tests',
    python_requires='>=3.6',
    zip_safe=False,
    url='https://github.com/rsouza01/enigma-machine',

)
