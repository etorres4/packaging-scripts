import setuptools

# ========== Constants ==========
EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
SCRIPTS = ["bin/addpkg", "bin/delpkg", "bin/fqo", "bin/pug2"]


# ========== Functions ==========
with open("README.rst", "r") as fh:
    long_description = fh.read()


# ========== Package Setup ==========
setuptools.setup(packages=PACKAGES)
