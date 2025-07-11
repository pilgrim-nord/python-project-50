from typing import Any, Dict, List


def format_value(value: Any, depth: int) -> str:
    if isinstance(value, dict):
        lines = ['{']
        for key in sorted(value.keys()):
            line = (
                f"{' ' * (depth * 4 + 8)}{key}: "
                f"{format_value(value[key], depth + 1)}"
            )
            lines.append(line)
        lines.append(f"{' ' * (depth * 4 + 4)}}}")
        return '\n'.join(lines)
    elif value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    elif value == '':
        return ''
    else:
        return str(value)


def stylish(diff: List[Dict[str, Any]], depth: int = 0) -> str:

    lines = []
    base_indent = ' ' * (depth * 4)

    for node in sorted(diff, key=lambda x: x['key']):
        key = node['key']
        op = node['operation']

        if op == 'nested':
            nested_value = stylish(node['value'], depth + 1)
            lines.append(f"{' ' * (depth * 4 + 4)}{key}: {nested_value}")
        elif op == 'same':
            value = format_value(node['value'], depth)
            lines.append(f"{' ' * (depth * 4 + 4)}{key}: {value}")
        elif op == 'added':
            value = format_value(node['new'], depth)
            lines.append(f"{' ' * (depth * 4 + 2)}+ {key}: {value}")
        elif op == 'removed':
            value = format_value(node['old'], depth)
            lines.append(f"{' ' * (depth * 4 + 2)}- {key}: {value}")
        elif op == 'changed':
            old_value = format_value(node['old'], depth)
            new_value = format_value(node['new'], depth)
            lines.append(f"{' ' * (depth * 4 + 2)}- {key}: {old_value}")
            lines.append(f"{' ' * (depth * 4 + 2)}+ {key}: {new_value}")

    if depth == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    else:
        return '{\n' + '\n'.join(lines) + '\n' + base_indent + '}'