from gendiff.diff_tree import make_diff_tree
from gendiff.formatter.stylish import stylish
from gendiff.input_data import input_data


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = input_data(file_path1)
    data2 = input_data(file_path2)
    unformatted_diff = make_diff_tree(data1, data2)
    if format_name == "stylish":
        return stylish(unformatted_diff)
    else:
        return "Unsupported format"
