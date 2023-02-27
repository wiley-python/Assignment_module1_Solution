str1 = 'I am 25 years and 10 months old'
def question2(str1):
    # Retain Numbers in String
    # Using list comprehension + join() + isdigit()
    res1 = "".join([item for item in str1 if item.isdigit()])
    print(res1)
    return res1


question2(str1)
