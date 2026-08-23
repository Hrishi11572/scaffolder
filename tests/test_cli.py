from typer.testing import CliRunner

from scaffolder.cli import app


runner = CliRunner()


def test_dry_run(tmp_path):
    readme = tmp_path / "README.md"

    readme.write_text("""\
# Directory Structure

project/
    src/
        main.py
""")

    result = runner.invoke(
        app,
        [str(readme), str(tmp_path / "output"), "--dry-run"]
    )

    assert result.exit_code == 0
    assert "Would create : " in result.stdout
    assert not (tmp_path / "output").exists()
    
def test_build(tmp_path):
    readme = tmp_path / "README.md"
    output = tmp_path / "output"

    readme.write_text("""\
# Directory Structure

project/
    src/
        main.py
""")

    result = runner.invoke(
        app,
        [str(readme), str(output)]
    )

    assert result.exit_code == 0

    assert (output / "project").is_dir()
    assert (output / "project" / "src").is_dir()
    assert (output / "project" / "src" / "main.py").is_file()
    
    
def test_force_allows_non_empty_target(tmp_path):
    readme = tmp_path / "README.md"
    output = tmp_path / "output"

    readme.write_text("""\
# Directory Structure

project/
    main.py
""")

    output.mkdir()
    existing = output / "existing.txt"
    existing.write_text("do not delete")

    result = runner.invoke(
        app,
        [str(readme), str(output), "--force"]
    )

    assert result.exit_code == 0

    assert existing.is_file()
    assert existing.read_text() == "do not delete"

    assert (output / "project" / "main.py").is_file()
    
def test_non_empty_target_without_force_fails(tmp_path):
    readme = tmp_path / "README.md"
    output = tmp_path / "output"

    readme.write_text("""\
# Directory Structure

project/
    main.py
""")

    output.mkdir()
    (output / "existing.txt").write_text("keep me")

    result = runner.invoke(
        app,
        [str(readme), str(output)]
    )

    assert result.exit_code != 0
    assert (output / "existing.txt").is_file()
    assert not (output / "project").exists()
    
def test_missing_markdown_file(tmp_path):
    missing_file = tmp_path / "README.md"
    output = tmp_path / "output"

    result = runner.invoke(
        app,
        [str(missing_file), str(output)]
    )

    assert result.exit_code != 0
    assert not output.exists()