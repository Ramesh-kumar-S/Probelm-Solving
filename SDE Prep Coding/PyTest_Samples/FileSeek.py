with open("Seek.txt","r") as f:
    # print(f.tell())
    f.seek(5)
    # print(f.tell())
    # print(f.read())
    # print(f.tell())
    print(f.readlines())
    print(f.fileno())
