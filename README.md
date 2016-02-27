Boids
===
An implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406) produced for the University College London course [MPHYG001: Research Software Engineering With Python](http://development.rc.ucl.ac.uk/training/engineering/).

Installation
---
To install from source run `python setupy.py install`. Or to install from github use `pip install
git+git://github.com/MikeVasmer/bad-boids`. To uninstall run
`pip uninstall boids`
if installed using `pip` or manually delete the files if installed using `
setup.py`.

Usage
---
Once installed run the program using the command:

`boids [-h --help] [-f --file FILE]`
- The `--help` flag prints the usage instructions.
- The `--file` flag allows the specify a configuration file, in yaml format.
- When no arguments are given the program will run with default parameters and an example configuration file (containing the default parameters) will be saved in the current directory.
