# def searcher(nums):                                       30 - PROBLEM
#     for x in nums:
#         if x == 0:
#             return True
#     return False

# nums = [1, 9, 4, 5]
# print(nums)
# print(searcher(nums))



# def factorial(num):                                        31 - PROBLEM
#     factor = 1
#     x = 1
#     while x <= num:
#         factor = factor * x
#         x += 1
#     return factor

# num = int(input("Enter number: "))
# print(factorial(num))



# def adder(num):                                           32 - PROBLEM
#     sum = 0
#     while num > 0:
#         sum += num % 10
#         num //= 10
#     return sum

# num = int(input("Enter number: "))
# print(adder(num))



# def counter(num):                                         33 - PROBLEM
#     count = 0
#     while num > 0:
#         count += 1
#         num //= 10
#     return count

# num = int(input("Enter number: "))
# print(counter(num))



# def reverser(num):                                        34 - PROBLEM
#     reverse = 0
#     while num > 0:
#         reverse = reverse * 10 + num % 10
#         num //= 10
#     return reverse

# num = int(input("Enter number: "))
# print(reverser(num))