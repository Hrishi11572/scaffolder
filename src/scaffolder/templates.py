from pathlib import Path 

PYTHON_TEMPLATE = """\
def main():
    pass


if __name__ == "__main__":
    main()
"""

CPP_TEMPLATE = """\
#include <iostream>

int main() {
    return 0;
}
"""

TEMPLATES = {
    ".py": PYTHON_TEMPLATE,
    ".cpp": CPP_TEMPLATE,
    ".hpp": CPP_TEMPLATE,
}

def get_template(filename):
    suffix = Path(filename).suffix
    return TEMPLATES.get(suffix)


if __name__ == "__main__": 
    
    st = get_template("main.py")
    print(st)