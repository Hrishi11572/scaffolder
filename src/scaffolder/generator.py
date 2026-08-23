from pathlib import Path 
from .model import Node, NodeType
from .templates import get_template

def generator(root : Node, target, template_dir=None): 
    root_path = Path(target) / root.name
    
    if root.type == NodeType.DIRECTORY: 
        root_path.mkdir(parents=True, exist_ok=True)
    else: 
        template = get_template(root.name, template_dir)
        
        if template is not None: 
            root_path.write_text(template) 
        else: 
            root_path.touch()
        
        
    for child in root.children: 
        generator(child, root_path, template_dir)
