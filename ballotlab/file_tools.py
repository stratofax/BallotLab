# Get properties of the file system
from inspect import getsourcefile
import os


class FileTools:
    code_dir = os.path.dirname(getsourcefile(lambda: 0))
    module_dir = os.path.realpath(os.path.join(code_dir, os.pardir))
