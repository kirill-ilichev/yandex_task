first_list = [1, 2, 3, 4, 5]
second_list = [4, 5, 5, 6, 7, 8, 9, 10]

assert list(set(first_list).difference(second_list)) == [1, 2, 3]
