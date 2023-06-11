import argparse
import shutil
import pathlib
import os

this_directory = pathlib.Path(__file__).parent.absolute()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="c++-bootstrap", 
        description="initializes new C++ project in the given directory"
    )
    parser.add_argument("projectname")
    projectname: str = parser.parse_args().projectname

    destination = pathlib.Path().absolute() / projectname

    shutil.copytree(
        this_directory, 
        destination, 
        dirs_exist_ok=False, 
        ignore=shutil.ignore_patterns(
            ".git", "c++-*.py"
        )
    )

    print("Initialized new project {} at {}".format(projectname, destination.parent))
