import setuptools
import subprocess

with open("README.rst", "r") as fh:
    long_description = fh.read()

def get_version():
    cmd = 'printf "%s" "$(git describe --long | sed "s/\([^-]*-\)g/r\1/;s/-/./g")"'
    return subprocess.run(cmd, shell=True, text=True).stdout

setuptools.setup(
    name="packaging_scripts",
    version=get_version(),
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
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
)
