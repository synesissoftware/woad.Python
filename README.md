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


## Installation

Install via **pip**:

```
pip install woad
```

Use via **import**:

```Python
import woad
```


## Components

**woad.Python** currently ships the **`woad`** package and version metadata (`woad.__version__`). Colour codes, TTY/stream gating, and Windows virtual-terminal opt-in are not implemented in this 0.0.0 skeleton.


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

* [**woad.Ruby**](https://github.com/synesissoftware/woad.Ruby/)
* [**woad.Rust**](https://github.com/synesissoftware/woad.Rust/)


### License

**woad.Python** is released under the 3-clause BSD license. See [LICENSE](./LICENSE) for details.


<!-- ########################### end of file ########################### -->
