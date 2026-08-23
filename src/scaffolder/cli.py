import typer 
from extractor import extract_structure
from generator import generator
from parser import parse_structure
from pathlib import Path 


def build(markdown_file: str, target: str):
    markdown = Path(markdown_file).read_text()
    
    structure = extract_structure(markdown)
    root = parse_structure(structure)
    generator(root, target)

if __name__ == "__main__":
    typer.run(build)