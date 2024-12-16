Res = []


def index_all(datas, num):
    for index, data in enumerate(datas):
        if data == num:
            Res.append(index)
        elif isinstance(data, list):
            index_all(data, num)


example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
index_all(example, 2)

"""
Iterate over lists
check if the element is list
call the function again
"""
