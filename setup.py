import os
import setuptools


# recursively load package files
def package_files(directory):
    paths = []
    for (path, _, filenames) in os.walk(directory):
        for filename in filenames:
            if not filename.endswith('.py'):
                paths.append(os.path.join('..', path, filename))
    return paths

# read long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NFixDB",
    version="2.0.0",
    author="Jose L. Figueroa III, Richard A. White III",
    author_email="jlfiguer@charlotte.edu",
    description="A comprehensive integrated database for robust 'omics analysis of diazotrophs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/raw-lab/nfixdb",
    scripts=['bin/nfixdb-workflow.py',],                                      # scripts to copy to 'bin' path
    packages=['nfixdb'],                                         # list of packages, installed to site-packages folder
    package_dir=dict(nfixdb='lib'),                              # dict with 'package'='relative dir'
    package_data=dict(nfoxdb=package_files('lib/')),             # add non-python data to package, relative paths
    license="BSD License",  # metadata
    platforms=['Unix'],     # metadata
    classifiers=[           # This is the new updated way for metadata (PyPi??), but old way seems to still be used in some of the output
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
    ],
    python_requires='>=3.8',
    install_requires=[
            'setuptools',
            'configargparse',
            'pandas',
            'pyhmmer',
            'biopython',
            ],
)
