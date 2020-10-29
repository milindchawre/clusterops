from setuptools import setup, find_packages

with open("README.md", encoding="UTF-8") as f:
    readme = f.read()

setup(
    name="cluster-ops",
    version="0.1.0",
    description="CLI to start/stop AWS resources",
    long_description=readme,
    author="Milind",
    author_email="milindchawre@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["boto3"],
    entry_points={
        "console_scripts": [
            "cluster-ops=clusterops.cli:main",
        ],
    },
)
