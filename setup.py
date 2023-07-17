import io
import os
from setuptools import setup, find_packages

NAME = "nutel_BSM"
DESCRIPTION = (
    "Code for aiding in calculating neutrino telescope responses to BSM fluxes"
)
MAINTAINER = "Jeff Lazar"
MAINTAINER_EMAIL = "jlazar@icecube.wisc.edu"
URL = "https://github.com/jlazar17/nutel_vsm"
LICENSE = "LGPL3"

here = os.path.abspath(os.path.dirname(__file__))

def read(path, encoding="utf-8"):
    with io.open(path, encoding=encoding) as f:
        content = f.read()
    return content

def get_install_requirements(path):
    content = read(path)
    requirements = [
        req for req in content.split("\n") if req != "" and not req.startswith("#")
    ]
    return requirements

NSTALL_REQUIRES = get_install_requirements(os.path.join(here, "requirements.txt"))

setup(
    name=NAME,
    #version=VERSION,
    description=DESCRIPTION,
    #long_description=LONG_DESCRIPTION,
    #long_description_content_type="text/markdown",
    url=URL,
    author=MAINTAINER,
    author_email=MAINTAINER_EMAIL,
    license=LICENSE,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=INSTALL_REQUIRES,
    setup_requires=["setuptools>=34.4.0"],
)
