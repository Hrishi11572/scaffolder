from scaffolder.parser import parse_structure
from scaffolder.model import NodeType
import pytest 


def test_single_root(): 
    root = parse_structure("project/")
    
    assert root.name == "project"
    assert root.type == NodeType.DIRECTORY 
    assert root.children == []

    
def test_nested_directory():
    text = """\
project/
    src/
"""

    root = parse_structure(text)

    assert root.name == "project"
    assert len(root.children) == 1

    src = root.children[0]

    assert src.name == "src"
    assert src.type == NodeType.DIRECTORY
    
    
def test_multiple_children():
    text = """\
project/
    src/
        main.cpp
        utils.cpp
"""

    root = parse_structure(text)

    src = root.children[0]

    assert len(src.children) == 2
    assert src.children[0].name == "main.cpp"
    assert src.children[1].name == "utils.cpp"

    assert src.children[0].type == NodeType.FILE
    assert src.children[1].type == NodeType.FILE
    
def test_sibling_directories():
    text = """\
project/
    src/
        main.cpp
    tests/
        test_main.cpp
"""

    root = parse_structure(text)

    assert len(root.children) == 2

    src = root.children[0]
    tests = root.children[1]

    assert src.name == "src"
    assert tests.name == "tests"

    assert src.children[0].name == "main.cpp"
    assert tests.children[0].name == "test_main.cpp"

def test_multiple_roots():
    text = """\
project/
    src/
other_project/
"""

    with pytest.raises(ValueError, match="two roots"):
        parse_structure(text)
        
def test_empty_input():
    assert parse_structure("") is None


def test_whitespace_only_input():
    assert parse_structure("   \n    \n") is None
    

def test_deep_nesting_and_unwinding():
    text = """\
project/
    src/
        utils/
            helper.py
        main.py
    tests/
        test_main.py
"""

    root = parse_structure(text)

    src = root.children[0]
    tests = root.children[1]

    utils = src.children[0]

    assert utils.name == "utils"
    assert utils.children[0].name == "helper.py"

    assert src.children[1].name == "main.py"
    assert tests.children[0].name == "test_main.py"