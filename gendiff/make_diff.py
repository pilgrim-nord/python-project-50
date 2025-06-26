from gendiff.input_data import input_data


def generate_diff(path_file1, path_file2):
    file1 = input_data(path_file1)
    file2 = input_data(path_file2)
    #
    # sorted_1 = dict(sorted(file1.items()))
    # sorted_2 = dict(sorted(file2.items()))
    keys = sorted(file1.keys() | file2.keys())
    diff_lines = []
    # diff_string = f'{{\n'
    #
    for key in keys:
        val1 = file1.get(key)
        val2 = file2.get(key)

        both_have = key in file1 and key in file2

        if not both_have:
            if key in file1:
                diff_lines.append(f"- {key}: {val1}")
            else:
                diff_lines.append(f"+ {key}: {val2}")
        elif val1 != val2:
            diff_lines.append(f"- {key}: {val1}")
            diff_lines.append(f"+ {key}: {val2}")
        else:
            diff_lines.append(f"  {key}: {val1}")

    return "{\n" + "\n".join(diff_lines) + "\n}"


