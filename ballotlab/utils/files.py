# Get properties of the file system
from inspect import getsourcefile
import os


class FileTools:
    package_name = "BallotLab"
    error_string = "Not executing in the expected package."
    # get the absolute path to this module
    code_dir = os.path.dirname(getsourcefile(lambda: 0))
    base_len = int(code_dir.find(package_name))
    if base_len == -1:
        raise Exception("Not executing in the expected package.")
    # if this module is part of the specified package, build the absolute path
    package_root = os.path.join(code_dir[:base_len], package_name)


if __name__ == "__main__":
    ftools = FileTools()
    print(ftools.code_dir)
    print(ftools.package_root)
