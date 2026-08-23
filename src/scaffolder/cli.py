import typer  # type: ignore
from extractor import extract_structure
from generator import generator
from parser import parse_structure
from pathlib import Path 


def build(
    markdown_file: str,
    target: str,
    templates : str | None = None,
    dry_run : bool = False, 
    force : bool = False 
):
    
    markdown_path = Path(markdown_file)
    
    # error handling here 
    if not markdown_path.exists(): 
        raise typer.BadParameter(
            f'Markdown file {markdown_file} does not exist.'
        )
        
    markdown = markdown_path.read_text()
    
    # added support to prevent overwriting a project directory 
    target_path = Path(target)
    if target_path.exists() and any(target_path.iterdir()) and not force:
        raise typer.BadParameter(
        f"Target directory '{target}' is not empty. "
        "Use --force to continue"
    )
    
    structure = extract_structure(markdown)
    
    # error handling here 
    if not structure.strip():
        raise typer.BadParameter(
            "No directory structure found in the Markdown file."
        )
        
    root = parse_structure(structure)
    
    # error handling here 
    if root is None: 
        raise typer.BadParameter(
            "Could not parse the directory structure."
        )
    
    
    if dry_run: 
        print("Would create : ")
        root.print_paths(target)
        return 
    
    generator(root, target, templates)

if __name__ == "__main__":
    typer.run(build)