# 1. Представлен список чисел. 
# Необходимо вывести элементы исходного списка, 
# значения которых больше предыдущего элемента. 
# Use comprehension.

# in
# 9

# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]

# in
# 10

# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

input_list = [15, 16, 2, 3, 1, 7, 5, 4, 10]
print(list(input_list[j] for j in range(1, len(input_list)) if input_list[j] > input_list[j - 1]))

from random import sample, randint
#
# def more_then(num):
#     my_list = sample(range(num * 3), num)
#     print(my_list)
#     return [my_list[num] for num in range(1, len(my_list)) if my_list[num]> my_list[num -1]]
#
# print(more_then(int(input())))


# def more_then(num):
#     orig_list = [randint(0, 1000) for _ in range(num)]
#     print(orig_list)
#     return[num for i, num in enumerate(orig_list[1:]) if num > orig_list[i]]
#
# print(more_then(int(input())))
