from gendiff import generate_diff as generate_diff


def test_diff_1():
    file_1 = './tests/fixtures/file1.json'
    file_2 = './tests/fixtures/file2.json'
    diff_data_file = open('./tests/fixtures/diff_data1.txt', 'r')
    diff_data = diff_data_file.read()
    result = generate_diff(file_1, file_2)
    assert diff_data == result


def test_empty():
    file_1 = './tests/fixtures/empty_file.json'
    file_2 = './tests/fixtures/empty_file.json'
    diff_data_file = open('./tests/fixtures/diff_data_empty.txt', 'r')
    diff_data = diff_data_file.read()
    result = generate_diff(file_1, file_2)
    assert diff_data == result
