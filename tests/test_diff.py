from gendiff import generate_diff as generate_diff


def test_diff_json():
    file_1 = './tests/fixtures/file1.json'
    file_2 = './tests/fixtures/file2.json'
    diff_data_file = open('./tests/fixtures/diff_data.txt', 'r')
    diff_data = diff_data_file.read()
    result = generate_diff(file_1, file_2)
    assert diff_data == result


def test_diff_yaml():
    file_1 = './tests/fixtures/file1.yaml'
    file_2 = './tests/fixtures/file2.yaml'
    diff_data_file = open('./tests/fixtures/diff_data.txt', 'r')
    diff_data = diff_data_file.read()
    result = generate_diff(file_1, file_2)
    assert diff_data == result
