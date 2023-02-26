with open("utils/dic.txt",mode="r",encoding="utf8") as rf:
    result = rf.readlines()[1:500000].strip()
    print(result)