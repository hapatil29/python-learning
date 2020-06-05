


# numbers = [3, 6, 2, 8, 4, 10]
# largest = numbers[0]
# for num in numbers:
#     if largest < num:
#         largest = num
# print(f'Largest number : {largest}')

###  List inside a list example
# matrix = [
#     [1,23,34],
#     [3,35,67],
#     [4,56,78]
# ]
#
# print(matrix[2][1])
#
# print("****************")
#
# for row in matrix:
#     for item in row:
#         print(item)

### Appending and inserting values to list
#
# numbers = [2, 4, 6, 23, 45]
# numbers.append(34)
# numbers.insert(2,0)
# print(numbers)
#
# ##remove an item in list, to do so pass the actual value
#
# numbers.remove(6)
# print(numbers)
#
#
# ##remove last item
# numbers.pop()
# print(numbers)
#
# numbers.clear()
# print(numbers)

#
# numbers1 = [2, 4, 6, 23, 4, 45]
# ## get index of a number in the list
# print(numbers1.index(4))
# ## find number which is not in list gives error, so use another method using "in"
# ###print(numbers1.index(60))
# print(60 in numbers1)
#
# ## count number of occurance in the list
# print(numbers1.count(4))
#
# #list sorting
# numbers1.sort()
# print(numbers1)
#
# numbers1.reverse()
# print(numbers1)
#
# ##to copy list to another list, any changes to original list it will not impact new list
# numbers2 = numbers1.copy()
#
# print(numbers2)


numbers3 = [2, 4, 6, 23, 4, 45, 2]

numbers4 = []

for item in numbers3:
    if item not in numbers4:
        numbers4.append(item)

print(numbers4)

