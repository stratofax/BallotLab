# BallotLab

A Pythonic repo of PDF-related code, part of the OSET BallotStudio project

## Getting Started

First, clone this repo into your a folder on your development computer. Then, follow these steps to set up your development environment: [How to set up a perfect Python project](https://sourcery.ai/blog/python-best-practices/)

TL;DR: here's a summary listing of the bash commands:

```bash
cd [vour/repo/directory]
# use pipx to install ensurepaht and pipenv
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install pipenv
# install development tools
pipenv install black isort --dev
pipenv install flake8 --dev
pipenv install mypy --dev
pipenv install pytest pytest-cov --dev
```
