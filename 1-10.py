# def counter(nums):                     1 - PROBLEM
#     count = 0
#     for x in nums:
#         if x % 2 != 0:
#             count += 1
#     return count

# nums = [1, 2, 3, 4, 5]
# print(nums)
# print(counter(nums))                     



# def counter(nums):                      2 - PROBLEM
#     sum = 0
#     for x in nums:
#         if x > 0:
#             sum += x
#     return sum

# nums = [-1, 2, -3, 4, -5]
# print(nums)
# print(counter(nums))



# def biggest(nums):                       3 - PROBLEM
#     max_i = 0
#     max_v = nums[0]
#     for x in range(len(nums)):
#         if max_v < nums[x]:
#             max_v = nums[x]
#             max_i = x
#     return max_i

# nums = [1, 4, 17, 8]
# print(nums)
# print(biggest(nums))



# def last(nums, target):                   4 - PROBLEM
#     last_i = 0
#     for x in range(len(nums)):
#         if nums[x] == target:
#             last_i = x
#     return last_i

 
# nums = [1, 4, 17, 8]
# target = 4
# print(nums)
# print(last(nums, target))



# def sec_biggest(nums):                       5 - PROBLEM
#     big = 0
#     sec = 0
#     for x in range(len(nums)):
#         print("big: ", big, " sec: ", sec)
#         if big < nums[x]:
#             sec = big
#             big = nums[x]
#         elif nums[x] > sec:
#             sec = nums[x]
#     return sec

# nums = [2, 4, 10, 1, 9, 2]
# print(nums)
# print(sec_biggest(nums))



# def multip(nums):                              6 - PROBLEM
#     mul = 1
#     for x in nums:
#         mul *= x
#     return mul

# nums = [1, 5, -2, 5]
# print(nums)
# print(multip(nums))



# def capital(text):                             7 - PROBLEM
#     count = 0
#     for x in text:
#         if x.isupper():
#             count += 1
#     return count

# text = "Hello World"
# print(text)
# print(capital(text))



# def consonants(text):                          8 - PROBLEM
#     count = 0
#     for x in text:
#         if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' or x == 'A' or x == 'E' or x == 'I' or x == 'O' or x == 'U':
#             pass
#         elif x >= 'a' and x <= 'z' or x >= 'A' and x <= 'Z':
#             print(x)
#             count += 1
        
#     return count

# text = "PYTHON"
# print(text)
# print(consonants(text))



# def count_words(text):                               9 - PROBLEM
#     count = 0
#     inside = False
#     for x in text:
#         print(x)
#         if x != " " and not inside:
#             count += 1
#             inside = True
#         elif x == " ":
#             inside = False
#     return count

# text = "Hello Wor ld     g"
# print(text)
# print(count_words(text))



# def number_count(text):                            10 - PROBLEM
#     count = 0
#     for x in text:
#         if x.isdigit():
#             count += 1
#     return count

# text = "Fr0stB1te"
# print(text)
# print(number_count(text))