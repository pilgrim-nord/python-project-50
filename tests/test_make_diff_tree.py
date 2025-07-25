import pprint
from pathlib import Path
from gendiff.diff_tree import make_diff_tree
from gendiff.input_data import input_data
from gendiff.formatter.stylish import stylish
from gendiff.formatter.plain import plain
from gendiff.formatter.json import json

test_data_dir = Path(__file__).parent / "test_data"

def test_make_diff_tree_json_stylish():

    expected_file_path = test_data_dir / "diff_result_stylish.txt"
    with open(expected_file_path, "r") as file:
        expected = file.read()
    file1_path_json = test_data_dir / "file1.json"
    file2_path_json = test_data_dir / "file2.json"
    data1_json = input_data(file1_path_json)
    data2_json = input_data(file2_path_json)
    diff = make_diff_tree(data1_json, data2_json)
    diff_stylish = stylish(diff)
    assert diff_stylish == expected

def test_make_diff_tree_yaml_stylish():

    expected_file_path = test_data_dir / "diff_result_stylish.txt"
    with open(expected_file_path, "r") as file:
        expected = file.read()

    file1_path_yaml = test_data_dir / "file1.yaml"
    file2_path_yaml = test_data_dir / "file2.yaml"
    data1_yaml = input_data(file1_path_yaml)
    data2_yaml = input_data(file2_path_yaml)
    diff = make_diff_tree(data1_yaml, data2_yaml)
    diff_stylish = stylish(diff)

    assert diff_stylish == expected


def test_plain():
    expected_file_path = test_data_dir / "diff_result_plain.txt"
    with open(expected_file_path, "r") as file:
        expected = file.read()
    file1_path_json = test_data_dir / "file1.json"
    file2_path_json = test_data_dir / "file2.json"
    data1_json = input_data(file1_path_json)
    data2_json = input_data(file2_path_json)
    diff = make_diff_tree(data1_json, data2_json)
    diff_plain = plain(diff)
    assert diff_plain == expected

def test_json():
    expected_file_path = test_data_dir / "diff_result_json.json"
    expected = input_data(expected_file_path)
    print('Ожидаемый')
    print(expected)
    file1_path_json = test_data_dir / "file1.json"
    file2_path_json = test_data_dir / "file2.json"
    data1_json = input_data(file1_path_json)
    data2_json = input_data(file2_path_json)
    diff = make_diff_tree(data1_json, data2_json)
    # print("Получившийся")
    # print(diff)
    # diff_json = json(diff)
    # pprint.pprint(diff_json)
    assert diff == expected