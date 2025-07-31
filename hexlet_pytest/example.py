def reverse(string):
    return string[::-1]


def read_file():
    text = open('d:/study/hexlet_pytest/tests/test_data/normal_text.txt').read()
    return text


print(reverse(read_file()))