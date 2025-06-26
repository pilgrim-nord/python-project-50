from pathlib import Path
from gendiff.make_diff import generate_diff


def test_generate_diff():
    # Путь к директории с фикстурами
    fixtures_dir = Path(__file__).parent / "fixtures"

    # Пути к файлам
    file1_path = fixtures_dir / "file1.json"
    file2_path = fixtures_dir / "file2.json"

    # Вызываем тестируемую функцию
    result = generate_diff(str(file1_path), str(file2_path))

    # Ожидаемый результат
    expected = """{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}"""

    assert result == expected