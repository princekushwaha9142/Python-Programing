# Find second largest number
my_list = [1, 2, 3, 4, 5]
unique_list = list(set(my_list))
unique_list.sort()
second_largest = unique_list[-2]
print(second_largest)