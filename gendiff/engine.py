import os
import json


def read_files(file_1, file_2):
    with open(os.path.abspath(file_1), 'r') as jsonFile_1, \
         open(os.path.abspath(file_2), 'r') as jsonFile_2:
        return json.load(jsonFile_1), json.load(jsonFile_2)


def gen_unique_keys(keys_1, keys_2):
    """Generate list of unique keys for both files"""

    unique_keys = []
    for key in keys_1:
        if key not in unique_keys:
            unique_keys.append(key)
        for key in keys_2:
            if key not in unique_keys:
                unique_keys.append(key)
    return sorted(unique_keys)


def generate_diff(file_1, file_2, format):
    """Display DIFF between two JSON files.

    Positional arguments:
    file_1, file2 - files to compare (Required)
    Optional arguments:
    format - output format (json by default)
    """
    object_1, object_2 = read_files(file_1, file_2)

#   Spaghetti code. Needs refactoring
    keys_1 = list(object_1.keys())
    keys_2 = list(object_2.keys())
    keys_list = gen_unique_keys(keys_1, keys_2)

    output_string = '''{\n'''

    for c_key in keys_list:
        if c_key in object_1.keys() and c_key in object_2.keys():
            if object_1[c_key] == object_2[c_key]:
                output_string += f'''    {c_key}: {object_1[c_key]}\n'''
            else:
                output_string += f'''  - {c_key}: {object_1[c_key]}\n'''
                output_string += f'''  + {c_key}: {object_2[c_key]}\n'''
        elif c_key in object_1.keys():
            output_string += f'''  - {c_key}: {object_1[c_key]}\n'''
        else:
            output_string += f'''  + {c_key}: {object_2[c_key]}\n'''

    output_string += '''}'''

    print(output_string)


def main(file_1, file_2, format):
    generate_diff(file_1, file_2, format)


if __name__ == '__main__':
    main()
