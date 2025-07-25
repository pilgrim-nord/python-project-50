from pathlib import Path
from gendiff.formatter.plain import plain
from gendiff.generate import generate_diff
from gendiff.formatter.stylish import stylish
test_data_dir = Path(__file__).parent / "test_data"

def test_generate_diff():
    expected_file_path = test_data_dir / "diff_result_stylish.txt"
    with open(expected_file_path, "r") as file:
        expected = file.read()
    file_path1 = test_data_dir / "file1.json"
    file_path2 = test_data_dir / "file2.json"
    diff = generate_diff(file_path1, file_path2)

    assert diff == expected