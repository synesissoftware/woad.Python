# woad.Python <!-- omit in toc -->

Minimal ANSI terminal colour codes, for Python

![Language](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![PyPI](https://img.shields.io/pypi/v/woad.svg)](https://pypi.org/project/woad/)
[![GitHub release](https://img.shields.io/github/v/release/synesissoftware/woad.Python.svg)](https://github.com/synesissoftware/woad.Python/releases/latest)
[![Last Commit](https://img.shields.io/github/last-commit/synesissoftware/woad.Python)](https://github.com/synesissoftware/woad.Python/commits/master)
[![CI](https://github.com/synesissoftware/woad.Python/actions/workflows/python-package.yml/badge.svg)](https://github.com/synesissoftware/woad.Python/actions/workflows/python-package.yml)
![Python](https://img.shields.io/badge/Python-2.7%20%7C%203.8+-lightgrey)


## Table of Contents <!-- omit in toc -->

- [Introduction](#introduction)
- [Developer Experience](#developer-experience)
- [Installation](#installation)
- [Components](#components)
- [Project Information](#project-information)
  - [Where to get help](#where-to-get-help)
  - [Contribution guidelines](#contribution-guidelines)
  - [Dependencies](#dependencies)
    - [Efferent (fan-out)](#efferent-fan-out)
    - [Development Dependencies](#development-dependencies)
    - [Afferent (fan-in)](#afferent-fan-in)
  - [Related projects](#related-projects)
  - [License](#license)


## Introduction

**woad** provides the smallest useful set of fixed ANSI SGR colour sequences for library authors. It is not a console or TUI framework.

**woad.Python** is the **Python** implementation. It supports **Python 2.7** and **Python 3.8+**.


## Developer Experience

**Python 2.7** or **Python 3.8+** is required. The library uses the standard library only. From a checkout:

```bash
python -m unittest discover -s tests
python examples/conditional.py
```

The smallest useful call prints a sequence only when the stream supports colour:

```Python
import sys

import woad

stream = sys.stdout
green = woad.seq_for(stream, woad.FG_GREEN)
reset = woad.seq_for(stream, woad.RESET)

print(green + "ok" + reset)
```

That is [examples/conditional.py](./examples/conditional.py). Fixed sequences (`BOLD`, `BLINKING`, `FG_*`, `BG_*`) always contain the SGR bytes. `colour_policy`, `supports_colour`, and `seq_for` apply the cached environment policy. `refresh` drops that cache. A `None` sequence yields `""`.


## Installation

Install via **pip**:

```
pip install woad
```

Use via **import**:

```Python
import woad

print(woad.FG_GREEN + "ok" + woad.RESET)
```


## Components

**woad.Python** ships fixed SGR sequences (`BLINKING`, `BOLD`, `RESET`, `FG_*`, `BG_*`, including bright variants) and the portable colour policy: `colour_policy`, `refresh`, `supports_colour`, and `seq_for`. On Unix a terminal supports colour when the policy is automatic and `TERM` is not `dumb`. Windows virtual-terminal mode and mintty PTY recognition are not implemented.


## Project Information


### Where to get help

[GitHub Page](https://github.com/synesissoftware/woad.Python "GitHub Page")


### Contribution guidelines

Defect reports, feature requests, and pull requests are welcome on https://github.com/synesissoftware/woad.Python.


### Dependencies


#### Efferent (fan-out)

None.


#### Development Dependencies

* [**pytest**](https://docs.pytest.org/)


#### Afferent (fan-in)

None (currently).


### Related projects

* [**woad**](https://github.com/synesissoftware/woad/)
* [**woad.Ruby**](https://github.com/synesissoftware/woad.Ruby/)
* [**woad.Rust**](https://github.com/synesissoftware/woad.Rust/)


### License

**woad.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->
