#!/usr/bin/python3
"""
    Write content to a file. If the file doesn't exist, it will be created.

    Parameters:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """


def write_file(filename="", text=""):
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
