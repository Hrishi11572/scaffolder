from pathlib import Path 
from model import Node, NodeType
from templates import get_template

def generator(root : Node, target): 
    root_path = Path(target)
    
    if root.type == NodeType.DIRECTORY: 
        root_path.mkdir(parents=True, exist_ok=True)
    else: 
        template = get_template(root.name)
        
        if template is not None: 
            root_path.write_text(template) 
        else: 
            root_path.touch()
        
        
    for child in root.children: 
        node_path = root_path /  child.name
        generator(child, node_path)
