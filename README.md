# BallotLab

A Pythonic repo of PDF-related code, part of the OSET BallotStudio project

## Getting Started

First, clone this repo into your a folder on your development computer. Then, at the command line, enter the following commands (Mac and Linux):

```bash
cd [vour/repo/directory]
# create a virtual environment
python3 -m venv venv
# activate the virtual environment
# note that if you're using another shell, besides bash,
# use a shell specific script, like "activate.csh" or "activate.fish"
source venv/bin/activate
```

These commands might be slightly different if you're using Windows or a shell besides bash.

If you created and activated your virtual environment, your command prompt should change to show you this.

Now, you can install the Python dependencies you need:

```bash
# Install PDFMiner to extract PDF data
python -m pip install pdfminer.six
```
