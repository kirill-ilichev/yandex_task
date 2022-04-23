array = [0, 1, 0, 0, 4, 5, 6, 7, 0, 8, -4, 0]

assert list(filter(lambda a: a != 0, array)) == [1, 4, 5, 6, 7, 8, -4]
