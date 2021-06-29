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
pipenv install isort --dev
# currently, black is pre-release so use the --pre flag
pipenv install black --pre --dev  
pipenv install flake8 --dev
pipenv install mypy --dev
pipenv install pytest pytest-cov --dev
```

### Install Required Python Packages

Once you've set up your development environment, install the required Python packages:

```bash
# Create PDF ballot files
pipenv install reportlab
# Add images to PDF files (replaces deprecated PIL)
pipenv install pillow
# (optional) extract text from PDFs
pipenv install pdfminer.six
```

## Project Structure

This Python project follows the current best practices, but also includes an "assets" folder, which contains fonts and images required to build ballots, including [Roboto from Google Fonts](https://fonts.google.com/specimen/Roboto)

## Election Specifications

This software conforms to the following US Election specifications:

* [usnistgov/ElectionResultsReporting at version2](https://github.com/usnistgov/ElectionResultsReporting/tree/version2)
