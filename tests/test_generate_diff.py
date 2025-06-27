from pathlib import Path
from gendiff.make_diff import generate_diff


# Ожидаемый результат

def test_generate_diff_json():

    fixtures_dir = Path(__file__).parent / "test_data"

    expected_file_path = fixtures_dir / "result.txt"
    with open(expected_file_path, "r", encoding="utf-8") as file:
        expected = file.read()

    # Пути к файлам
    file1_path = fixtures_dir / "file1.json"
    file2_path = fixtures_dir / "file2.json"

    # Вызываем тестируемую функцию
    result = generate_diff(str(file1_path), str(file2_path))



    assert result == expected

def test_generate_diff_yaml():

    fixtures_dir = Path(__file__).parent / "test_data"

    expected_file_path = fixtures_dir / "result.txt"
    with open(expected_file_path, "r", encoding="utf-8") as file:
        expected = file.read()

    # Пути к файлам
    file1_path = fixtures_dir / "file1.yaml"
    file2_path = fixtures_dir / "file2.yaml"

    # Вызываем тестируемую функцию
    result = generate_diff(str(file1_path), str(file2_path))


    assert result == expected