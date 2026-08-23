# autodir

autodir is a useful Python CLI tool that generates project
directory structures from a Markdown description.

Instead of manually creating directories and empty files, you can
describe the desired structure in a simple Markdown-style tree and let
autodir create it automatically.

## Features

-   Generate directories and files from a Markdown tree
-   Create starter templates for supported file types
-   Support custom templates
-   Preview changes with `--dry-run`
-   Safely generate into existing directories with `--force`
-   Simple command-line interface built with Typer
-   Designed to be easy to extend with additional templates and project
    structures

## Installation

Install autodir from PyPI:

``` bash
pip install autodir
```

Verify the installation:

``` bash
autodir --help
```

## Usage

The basic command is:

``` bash
autodir <markdown_file> <target>
```

For example:

``` bash
autodir README.md ./output
```

autodir reads the structure from `README.md` and creates it inside
`./output`.

## Defining a Project Structure

The directory structure must be written under a `# Directory Structure` heading in your Markdown file.

For example:

    # Directory Structure

    project/
        src/
            main.py
            utils.cpp
        tests/
            test_main.py
        pyproject.toml

Then run:

``` bash
autodir README.md ./output
```

The resulting directory will look like:

``` text
output/
└── project/
    ├── src/
    │   ├── main.py
    │   └── utils.cpp
    ├── tests/
    │   └── test_main.py
    └── pyproject.toml
```

## File Templates

autodir can create starter content for supported file types.

For example, a Python file is initialized with:

``` python
def main():
    pass


if __name__ == "__main__":
    main()
```

A C++ file is initialized with a minimal program:

``` cpp
#include <iostream>
using namespace std;

int main() {
    return 0;
}
```

Currently supported built-in templates include:

-   `.py`
-   `.cpp`
-   `.hpp`

Files without a matching template are created as empty files.

## Dry Run

Use `--dry-run` to preview what autodir would create without
modifying the target directory:

``` bash
autodir README.md ./output --dry-run
```

This is useful for checking a structure before actually generating it.

## Existing Directories

By default, autodir avoids generating into a non-empty target
directory.

If you intentionally want to generate into an existing non-empty
directory, use:

``` bash
autodir README.md ./output --force
```

`--force` allows generation to proceed without deleting unrelated files
already present in the target directory.

## Custom Templates

autodir also supports supplying a custom template directory.

A template directory can contain files whose extensions correspond to
the file types you want to customize.

For example:

``` text
templates/
├── .py
├── .cpp
└── .hpp
```

When a matching template is available, autodir uses its contents
instead of the built-in template.

## Project Architecture

The project is organized into several components:

``` text
src/autodir/
├── cli.py
├── extractor.py
├── generator.py
├── model.py
├── parser.py
└── templates.py
```

### Parser

Converts the textual directory structure into a tree representation.

### Model

Defines the tree nodes used to represent files and directories.

### Extractor

Extracts the relevant directory structure from the Markdown input.

### Generator

Traverses the parsed tree and creates the corresponding directories and
files.

### Templates

Provides built-in and custom file templates.

### CLI

Provides the user-facing command-line interface.

## Development

Clone the repository and create a virtual environment:

``` bash
git clone https://github.com/Hrishi11572/autodir.git
cd autodir

python3 -m venv .venv
source .venv/bin/activate
```

Install the development dependencies and package:

``` bash
pip install -e .
```

Run the test suite:

``` bash
python -m pytest
```

Run tests with coverage:

``` bash
python -m pytest --cov=autodir --cov-report=term-missing
```

## Building the Package

Install the build tools:

``` bash
python -m pip install build
```

Build the source distribution and wheel:

``` bash
python -m build
```

The generated packages will be placed in:

``` text
dist/
```

## Why autodir?

Project setup often involves repetitive work: creating directories,
adding placeholder files, and writing standard boilerplate. autodir
separates the description of a project from the process of creating it.

You describe the structure once, and autodir turns that description
into a real filesystem structure.

## License

MIT License
