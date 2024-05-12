import setuptools

EXCLUDED_PACKAGES = ["test", "tests"]
PACKAGES = setuptools.find_packages(exclude=EXCLUDED_PACKAGES)
SCRIPTS = [
    "packaging_scripts/bin/addpkg",
    "packaging_scripts/bin/delpkg",
    "packaging_scripts/bin/fqo",
    "packaging_scripts/bin/pug2",
]
setuptools.setup(scripts=SCRIPTS, packages=PACKAGES)
