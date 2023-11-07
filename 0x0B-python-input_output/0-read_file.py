#!/usr/bin/python3

"""
reads the content of a text file (UTF-8 encoded)

Parameters:
    filename (str, optional): The name of the file to be read.
Usage:
    You can use this function by calling it with the `filename` parameter

Example:
    read_file("your_text_file.txt")

Note:
    - The function uses the 'with' statement to ensure proper file handling.
    - It doesn't handle exceptions.
    - This function doesn't require importing any additional modules.
"""


def read_file(filename=""):
    """
        read_file reads teaxt file and prints to stdout
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end='')
