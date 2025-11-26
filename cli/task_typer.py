"""
Implement a simple command line utility that will return a size of a given file, for example:

    uv run typer cli/task_typer.py run main.py

should print something like:

    Size of the file is 93 bytes

Accept two arguments:
- name (str) - mandatory, name of the file.
*- recurse (bool) - optional, default false.
If a recurse is false and path given in name is a directory, return error message.
If a recurse is true and path given is NOT a directory, return error message.
If a recurse is true and path given is a directory, calculate and sum size of all files - use files_in_directory function.
"""
import os
import os.path
import pathlib

import typer


app = typer.Typer()


# TODO code


def get_size_of_file(path_name: str) -> int:
    """Returns size of file in bytes"""
    return os.path.getsize(path_name)

def is_directory(path_name: str) -> bool:
    """Returns true if a given path is a directory."""
    return os.path.isdir(path_name)

def files_in_directory(path_name: str) -> list[str]:
    """Returns a list of all files in a given directory"""
    dir = pathlib.Path(path_name)
    file_names = []
    for root, _dirs, files in dir.walk(path_name):
        if str(root).startswith(".") or "__pycache__" in str(root):
            continue
        if files:
            file_names.extend([
                str(root / fname) for fname in files
            ])
    return file_names

if __name__ == "__main__":
    app()
