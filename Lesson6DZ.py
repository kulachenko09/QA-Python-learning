2.

import copy
#
# ordersList = [
#          [34587, 'Learning Python, Mark Lutz', 4, 40.95],
#          [98762, 'Programming Python, Mark Lutz', 5, 56.80],
#          [77226, 'Head First Python, Paul Barry', 3, 32.95],
#          [88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
#          ]
#
# print(ordersList)
#
# def getOrdersData(orders):
#     ordersCopy = copy.deepcopy(orders)
#     def totalCalculation(item):
#         item[3] = item[2]*item[3]
#         if item[3] < 100:
#             item[3] += 10
#         return tuple(item)
#
#     ordersSum = list(map(totalCalculation, ordersCopy))
#
#     return ordersSum
#
# print(getOrdersData(ordersList))
#
# def addSomeBooks(orders):
#     newOrders = [
#                     [24387, ' на русском', 2, 4.59],
#                     [18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
#                     [87236, 'C Programming Absolute Beginner\'s Guide', 1, 23.55],
#                     [58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
#                  ]
#     ordersSource = orders + newOrders
#     return ordersSource
#
#
# print(addSomeBooks(ordersList))
#
#
# def sortOrders(orders):
#     ordersCopy = copy.deepcopy(orders)
#     ordersCopy.sort(key=lambda x: x[3])
#     return ordersCopy
#
#
# print(sortOrders(addSomeBooks(ordersList)))
#
#
# def filterOrders(orders):
#     ordersCopy = copy.deepcopy(orders)
#     ordersFiltered = list(filter(lambda x: x[2] > 5, ordersCopy))
#     return ordersFiltered
#
# print(filterOrders(sortOrders(addSomeBooks(ordersList))))



#1.  Вам дан код сортировки
# пузырьком, однако он
# работает неверно, там
# допущена ошибка.
# Используя дебагер,
# найдите и исправьте
# ошибку.

def buble_sort(l):
    t = l.copy()

    # ошибка была в количестве итераций - отнимаем 1
    for n in range(len(t)-1):
        # отнимаем 1
        for i in range(len(t)-n-1):
            # нужно увеличивать индексы на 1 и изменяем n на i
            if t[i] > t[i+1]:
                t[i], t[i+1] = t[i+1], t[i]
    return t

# nums = [4, 1, 6, 3, 2, 7, 8]
# sorted = buble_sort(nums)
# print(sorted)

# test1
print(buble_sort([12, 65, 1, 4, 15, 45, 77, 10, 14, 11]))

# test2
print(buble_sort([2, 99, 100, 5, 6, 11, 7]))

# test3
print(buble_sort([22, 75, 54, 14, 257, 256, 877, 250, 36, 888]))

# test4
print(buble_sort([44, 7, 72, 86, 62, 65, 66, 99, 99, 100]))

# test5
print(buble_sort([89, 44, 1, 4, 15, 45]))
