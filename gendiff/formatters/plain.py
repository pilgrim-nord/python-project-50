def format_value(value):

    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def plain(diff, path=""):
    result = []

    def get_full_path(key):
        return f"{path}.{key}" if path else key

    for node in diff:
        key = node['key']
        full_key = get_full_path(key)
        operation = node['operation']

        if operation == 'nested':
            child_str = plain(node['value'], full_key)  # получаем строку
            result.append(child_str)
        elif operation == 'added':
            value = format_value(node['new'])
            result.append(
                f"Property '{full_key}' was added with value: {value}")
        elif operation == 'removed':
            result.append(f"Property '{full_key}' was removed")
        elif operation == 'changed':
            old_value = format_value(node['old'])
            new_value = format_value(node['new'])
            result.append(
                f"Property '{full_key}' was updated. "
                f"From {old_value} to {new_value}"
            )

    return '\n'.join(result)



