from scaffolder.parser import parse_structure
from scaffolder.model import NodeType


def test_single_root(): 
    root = parse_structure("project/")
    
    assert root.name == "project"
    assert root.type == NodeType.DIRECTORY 
    assert root.children == []