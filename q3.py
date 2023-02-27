import string

str1 = '/*Jon is @developer & musician!!'


def question3(str1):
    replace_char = '#'
    for char in string.punctuation:
        str1 = str1.replace(char, replace_char)
    return str1


print(question3(str1))

