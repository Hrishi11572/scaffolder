from pathlib import Path 

PYTHON_TEMPLATE = """\
def main():
    pass


if __name__ == "__main__":
    main()
"""

CPP_TEMPLATE = """\
#include <iostream>
using namespace std; 

int main() {
    return 0;
}
"""


def get_template(filename, template_dir=None):
    TEMPLATES = {
        ".py": PYTHON_TEMPLATE,
        ".cpp": CPP_TEMPLATE,
        ".hpp": CPP_TEMPLATE,
    }   
    
    suffix = Path(filename).suffix 
    
    if template_dir is None: 
        return TEMPLATES.get(suffix)

    if template_dir is not None: 
        template_path = Path(template_dir) / suffix 
        
        if template_path.exists(): 
            return template_path.read_text()

    return None


if __name__ == "__main__": 
    
    print(get_template("main.py"))
    print(get_template("main.cpp"))

    print(get_template("main.py", "../../templates"))
    print(get_template("main.cpp", "../../templates"))
    print(get_template("main.xyz", "../../templates"))