nums = [1 , -2, -4, 6]
positive_nums = [num for num in nums if num >=0]
negative_nums = [num for num in nums if num <0]

even_nums = [num for num in nums if num % 2 == 0]
odd_nums = [num for num in nums if num % 2 == 1]

print(positive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

