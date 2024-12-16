import re


def is_palindrom(word):
    charsAlone = "".join(list(filter(lambda x: x.isalpha(), list(word))))

    regexCharsAlone = "".join(re.findall(r'[a-z]+', word.lower()))
    # print(regexCharsAlone)

    print(charsAlone.lower() == charsAlone[::-1].lower())


is_palindrom("Go hang a salami, I’m a lasagna hog.")
is_palindrom("hello world")
