from scaffolder.extractor import extract_structure
from scaffolder.parser import parse_structure
from scaffolder.generator import generator

MARKDOWN = """
# Project

# Directory Structure

project/
    src/
        main.py
        utils.cpp
    tests/
        test.py
    README.md

# Installation

Some instructions.
"""

structure = extract_structure(MARKDOWN)
root = parse_structure(structure)

generator(root, "../../outputs")
