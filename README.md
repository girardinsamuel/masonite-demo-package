# Demo Package

<p align="center">
<img src="https://i.imgur.com/rEXcoMn.png" width="130px">
</p>

<p align="center">

[![Test Application](https://github.com/girardinsamuel/masonite-demo-package/workflows/Test%20Application/badge.svg?branch=master)](https://github.com/girardinsamuel/masonite-demo-package/actions)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/girardinsamuel/masonite-demo-package/branch/master/graph/badge.svg)](https://codecov.io/gh/girardinsamuel/masonite-demo-package/)
<img src="https://img.shields.io/badge/python-3.6+-blue.svg" alt="Python Version">
<a href="https://pypi.org/project/masonite-demo-package/"><img alt="PyPI" src="https://img.shields.io/pypi/v/masonite-demo-package"></a>

</p>

## Introduction

Demo package to show Masonite cookiecutter scaffolding result.

**This package has been generated with [Cookiecutter Masonite Package](https://github.com/girardinsamuel/cookiecutter-masonite-package).**

## Features

- _Add your package main features here_
- _and here_

## Official Masonite Documentation

New to Masonite ? Please first read the [Official Documentation](https://docs.masoniteproject.com/).
Masonite strives to have extremely comprehensive documentation 😃. It would be wise to go through the tutorials there.
If you find any discrepencies or anything that doesn't make sense, be sure to comment directly on the documentation to start a discussion!

Also be sure to join the [Slack channel](http://slack.masoniteproject.com/)!

## Installation

```bash
pip install masonite-demo-package
```

## Configuration

Add DemoPackageProvider to your project in `config/providers.py`:

```python
# config/providers.py
# ...
from masonite.demo_package import DemoPackageProvider

# ...
PROVIDERS = [
    # ...

    # Third Party Providers
    DemoPackageProvider,

    # ...
]
```

Then install OR publish the reqired package files (configuration, views ...):

```bash
python craft demo_package:install
```

OR (depending on your preferences)

```bash
python craft publish DemoPackageProvider
```

## Usage

_Explain how to use your package_

## Contributing

Please read the [Contributing Documentation](CONTRIBUTING.md) here.

## License

Demo Package is open-sourced software licensed under the [MIT license](LICENSE).
