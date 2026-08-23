from .parser import parse_structure

def find_indent(s : str):
    return len(s) - len(s.lstrip())

def extract_structure(markdown): 
    
    lines = markdown.splitlines()
    found_structure_heading = False
    structure = "" 
    
    for line in lines:
        
        if not line.strip(): 
            continue
        
        if found_structure_heading and line.strip().startswith("#"):
            break
        elif found_structure_heading :
            structure += (line + '\n') 
        
        if line.strip() == "# Directory Structure": 
            found_structure_heading = True
    
    # Processing the structure before returning 
    elements = structure.split("\n")
    base_indent = find_indent(elements[0])
    
    for i, element in enumerate(elements): 
        elements[i] = element[base_indent:] + '\n'        
    
    structure = "".join(elements)
    return structure 


if __name__ == "__main__": 
    
    MARKDOWN = '''
    
    # Hello World
        This is some random paragraph written here 
    
    # Init Project 
        Run some random command and be happy !
        
    # Directory Structure

        project/
            src/
                main.cpp
                utils.cpp
            
            tests/
                test_program.py
            README.md
    
    # Happy Journey 
    Some random things here and there!
    '''
    
    
    structure = extract_structure(MARKDOWN)
    root = parse_structure(structure)
    root.print_tree()