### Hexlet tests and linter status:
[![Actions Status](https://github.com/pletnev-aa/python-project-lvl3/workflows/hexlet-check/badge.svg)](https://github.com/pletnev-aa/python-project-lvl3/actions)
![example workflow](https://github.com/pletnev-aa/python-project-lvl3/actions/workflows/linter.yml/badge.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/63dc5f710f002f68894c/maintainability)](https://codeclimate.com/github/pletnev-aa/python-project-lvl3/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/63dc5f710f002f68894c/test_coverage)](https://codeclimate.com/github/pletnev-aa/python-project-lvl3/test_coverage)

# Pageload
### CLI-utility to download web pages

## Usage

```bash
$ pageload --help
usage: pageload [options] <url>

Download web-pages and saves localy

positional arguments:
  url                   url to download

optional arguments:
  -h, --help            help message
  -o OUTPUT, --output OUTPUT
                        output dir (default: [current directory])
  -l DEBUG, --log-level DEBUG
                        sets log level (default: WARNING)


$ pageload --output /var/tmp https://ru.hexlet.io/courses
/var/tmp/ru-hexlet-io-courses.html
```
