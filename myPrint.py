def printPretty(*args):
    char = ['*', '&', '%', '$', '@']
    import random
    y = random.randint(0, 4)
    print(char[y] * 22)
    for i in args:
        print(i)
    print(char[y] * 22)
