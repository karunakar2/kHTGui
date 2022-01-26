import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kHTGui",
    version="1.0.0",
    author="Karunakar",
    author_email="karunakar.kintada@gmail.com",
    description="GUI to select kHilltopConnector station and measurement",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hawkes-bay-rc/kHTGui",
    project_urls={
        "Bug Tracker": "https://github.com/hawkes-bay-rc/kHTGui/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU GPLv3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    #data_files=[('data',['data/openDataLinks.json'])],
    packages=setuptools.find_packages(where="src"), #+ ['config'],
    python_requires=">=3.6",
    install_requires=[
      'datetime', 'requests', 'requests_cache', 'defusedxml', 'numpy', 'pandas'
    ],
)