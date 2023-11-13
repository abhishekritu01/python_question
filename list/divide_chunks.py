
# def divide_chunks(l, n):
#     for i in range(0, len(l), n):
#         yield l[i:i + n]

# l = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]

# n = 5

# x = list(divide_chunks(l, n))

# print(x)


# -------------------chumks
def divide_chunks(lst):
    start = 0
    end = len(lst)
    step = 3

    for i in range(start, end, step):
        chunk = lst[i:i+step]
        print(chunk)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

divide_chunks(my_list)
