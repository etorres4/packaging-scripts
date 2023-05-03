import setuptools

# ========== Constants ==========
EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
SCRIPTS = ["bin/addpkg", "bin/delpkg", "bin/fqo", "bin/pug2"]


# ========== Functions ==========
with open("README.rst", "r") as fh:
    long_description = fh.read()


# ========== Package Setup ==========
setuptools.setup(
    name="packaging_scripts",
    version="1.7.1",
    author="Eric Russel Torres",
    author_email="erictorres4@protonmail.com",
    description="A set of scripts for automating pacman database interaction",
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
