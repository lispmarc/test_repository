import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="test_package",
    version="0.0.1",
    author="Marc Mertens",
    author_email="marc.mertens@skillpipe.com",
    description="A smallpackage to test actions on github",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lispmarc/test_package",
    project_urls={
        "Bug Tracker": "https://github.com/lispmarc/test_package/issues",
    },
    package_dir={"": "src"}, 
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)