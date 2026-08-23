from model import Node, NodeType

def parse_structure(text):
    '''
    for each line - 
        1. Calculate indent
        2. Calculate name
        3. Create Node
        4. Find its parent using stack
        5. Add it to parent
        6. Put current node on stack    
    '''
    
    lines = text.splitlines() 
    stack = [] 
    root = None 
    
    for line in lines: 
        if line.strip(): 
            indent = len(line) - len(line.lstrip())
            name = line.strip()
            node_type = NodeType.FILE if name[-1] != '/' else NodeType.DIRECTORY
            node = Node(name=name.rstrip("/"), type= node_type)
            
            if (root is not None) and (indent == 0): 
                raise ValueError("There can not be two roots in the directory structure!")
            
            if root is not None and root.type != NodeType.DIRECTORY:
                raise ValueError("Root must be a directory")
            
            
            if stack: 
                current_indent = indent 

                while stack and current_indent <= stack[-1][1]:
                    stack.pop()
                
                if stack:                     
                    stack[-1][0].add_child(node)
            else: 
                root = node 
            
            stack.append((node, indent))
            
    return root
            

if __name__ == "__main__":     
         
    text = '''project/
        src/
            main.cpp
        tests/
            test.cpp'''

    root = parse_structure(text)
    root.print_tree()