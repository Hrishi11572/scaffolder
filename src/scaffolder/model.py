from enum import Enum 
from dataclasses import dataclass, field 
from pathlib import Path 

class NodeType(Enum): 
    FILE = "file" 
    DIRECTORY = "directory"
    

@dataclass
class Node: 
    name: str 
    type : NodeType 
    children : list["Node"] = field(default_factory=list) 

    
    def add_child(self, node : "Node"): 
        self.children.append(node)
    
    def print_tree(self, indent=0): 
        name = self.name if self.type == NodeType.FILE else self.name + '/'
        print("  " * indent + name)
        
        for child in self.children: 
            child.print_tree(indent + 1) 
        
        return None 
    
    def print_paths(self, base_path): 
        current_path = Path(base_path) / self.name
        
        print(current_path)
        
        for child in self.children: 
            child.print_paths(current_path)

    
if __name__ == "__main__": 
    root = Node("project", NodeType.DIRECTORY) 
    src = Node("src", NodeType.DIRECTORY)
    main = Node("main", NodeType.FILE)
    
    src.add_child(main)
    root.add_child(src) 
    
    root.print_tree()