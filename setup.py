import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packaging_scripts",
    version="1.1.1",
    author="Eric Russel Torres",
    author_email="erictorres4@protonmail.com",
    description="A set of helpers for automating borg interaction",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    scripts=['bin/addpkg', 'bin/delpkg', 'bin/fqo'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
