from enum import Enum 
from dataclasses import dataclass, field 


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
        
        return 

    
if __name__ == "__main__": 
    root = Node("project", NodeType.DIRECTORY) 
    src = Node("src", NodeType.DIRECTORY)
    main = Node("main", NodeType.FILE)
    
    src.add_child(main)
    root.add_child(src) 
    
    root.print_tree()