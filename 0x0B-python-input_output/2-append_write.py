#!/usr/bin/python3
"""
    Append_write content to a file. If the file doesn't exist, it will be created.

    Parameters:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """


def append_write(filename="", text=""):
    """
    Append_write content to a file. If the file doesn't exist.
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
