#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file."""
import sys
from typing import List
from json import dumps
from os.path import exists

def save_to_json_file(my_obj: List[str], filename: str) -> None:
    """Save an object to a JSON file."""
    with open(filename, mode='w') as file:
        file.write(dumps(my_obj))

def load_from_json_file(filename: str) -> List[str]:
    """Load an object from a JSON file."""
    with open(filename, mode='r') as file:
        return file.read()

if __name__ == "__main__":
    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []
    
    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
