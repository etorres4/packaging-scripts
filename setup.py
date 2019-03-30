import setuptools

# ========== Constants ==========
PACKAGES = ["packaging_scripts"]
SCRIPTS = ["bin/addpkg", "bin/delpkg", "bin/fqo"]


# ========== Functions ==========
with open("README.rst", "r") as fh:
    long_description = fh.read()


# ========== Package Setup ==========
setuptools.setup(
    name="packaging_scripts",
    version="1.3.1",
    author="Eric Russel Torres",
    author_email="erictorres4@protonmail.com",
    description="A set of helpers for automating borg interaction",
    long_description=long_description,
    long_description_content_type="text/plain",
    url="",
    packages=PACKAGES,
    scripts=SCRIPTS,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
