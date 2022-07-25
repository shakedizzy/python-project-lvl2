import os
import json


def read_files(file_1, file_2):
    with open(os.path.abspath(file_1), 'r') as jsonFile_1, \
         open(os.path.abspath(file_2), 'r') as jsonFile_2:
        return json.load(jsonFile_1), json.load(jsonFile_2)


def gen_unique_keys(keys):
    """Generate list of unique keys for both files"""

    unique_keys = set(keys)
    return sorted(list(unique_keys))


def generate_diff(file_1, file_2, format):
    """Display DIFF between two JSON files.

    Positional arguments:
    file_1, file2 - files to compare (Required)
    Optional arguments:
    format - output format (json by default)
    """
    object_1, object_2 = read_files(file_1, file_2)

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

    print(output_string)


def main(file_1, file_2, format):
    generate_diff(file_1, file_2, format)


if __name__ == '__main__':
    main()
