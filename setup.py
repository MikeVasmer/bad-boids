from setuptools import setup, find_packages

setup(
    name = "Boids",
    version = "1.0.0",
    packages = find_packages(exclude=["*test"]),
    scripts = ["scripts/boids"],
    install_requires = ["matplotlib","numpy","yaml"],
    package_data = {"boids" : ["params.yaml"]}

    # metadata
    author = "Michael Vasmer",
    author_email = "michael.vasmer.15@ucl.ac.uk",
    description = "A package to simulate the flocking behaviour of birds",
    license = "MIT",
    keywords = "birds boids flocking"
)
