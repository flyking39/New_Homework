# the first and the most fundamental
# def counting():
#     for i in range(user_input):
#         list_of_stuff.pop(0)
#     print(list_of_stuff[0])
#
#
# list_of_stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# user_input = int(input('Enter the index of the item you are looking for: '))
# counting()




# second method with iterator utilization
# list_of_stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# y = filter(lambda x: x, list_of_stuff)
# user_input = int(input('Enter the index of the item you are looking for: '))
# for i in range(user_input + 1):
#     print(y.__next__())
# print(y)

# the third method
# list_of_stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# user_input = int(input('Enter the index of the item you are looking for: '))
#
#
# def function():
#     for x in list_of_stuff:
#         if x != list_of_stuff[user_input]:
#             print('not what you are looking for')
#         else:
#             yield x
#             break
#
#
# for t in function():
#     print(t)



# the fourth method
list_of_stuff = [1, 2, 3, 4, 5, 6, 7, 8, 9]
user_input = int(input('Enter the index of the item you are looking for: '))


def function():
    """
    function that searches for the item from the list using user index
    :return:
    """
    for x in list_of_stuff:
        try:
            if x == list_of_stuff[user_input]:
                yield x
                break
            else:
                continue
        except IndexError:
            print('you may have entered the number exceeding the max range of the storage')


for t in function():
    print(t)
