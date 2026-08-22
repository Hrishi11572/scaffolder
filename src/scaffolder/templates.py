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

    template_dir = Path(template_dir)

    for template_file in template_dir.iterdir():
        if template_file.suffix == suffix:
            return template_file.read_text()

    return None


if __name__ == "__main__": 
    
    st = get_template("main.cpp", template_dir="../../templates")
    print(st)