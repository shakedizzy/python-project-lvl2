from gendiff.lib.parser import read_file


def gen_unique_keys(keys):
    """Generate list of unique keys for both files"""

    unique_keys = set(keys)
    return sorted(list(unique_keys))


def generate_diff(file_1, file_2, format='json'):
    """Display DIFF between two JSON files."""

    object_1 = read_file(file_1)
    object_2 = read_file(file_2)

    keys = list(object_1.keys())
    keys.extend(list(object_2.keys()))

    keys_list = gen_unique_keys(keys)

    output_string = '''{\n'''

    for key in keys_list:
        if key in object_1.keys() and key in object_2.keys():
            if object_1[key] == object_2[key]:
                output_string += f'''    {key}: {object_1[key]}\n'''
            else:
                output_string += f'''  - {key}: {object_1[key]}\n'''
                output_string += f'''  + {key}: {object_2[key]}\n'''
        elif key in object_1.keys():
            output_string += f'''  - {key}: {object_1[key]}\n'''
        else:
            output_string += f'''  + {key}: {object_2[key]}\n'''

    output_string += '''}'''

    return output_string


def main(file_1, file_2, format):
    output_string = generate_diff(file_1, file_2, format)
    print(output_string)


if __name__ == '__main__':
    main()
