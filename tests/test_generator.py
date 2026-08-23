from scaffolder.parser import parse_structure
from scaffolder.generator import generator


def test_generate_directory_structure(tmp_path):
    text = """\
project/
    src/
        main.py
        utils.cpp
    tests/
        test_main.py
"""

    root = parse_structure(text)

    generator(root, tmp_path)

    assert (tmp_path / "project").is_dir()
    assert (tmp_path / "project" / "src").is_dir()
    assert (tmp_path / "project" / "src" / "main.py").is_file()
    assert (tmp_path / "project" / "src" / "utils.cpp").is_file()
    assert (tmp_path / "project" / "tests" / "test_main.py").is_file()