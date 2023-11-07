#!/usr/bin/python3
"""
    Write content to a file. If the file doesn't exist, it will be created.

    Parameters:
        filename (str): The name of the file to write to.
        content (str): The content to write to the file.
    """


def write_file(filename="", text=""):
    """
        Write in the text file or creat it if it 
        doesnt exist
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
