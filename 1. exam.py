


#  first exam

#  1. a  2. c  3. c  4. b  5.  c  6. d 

#####################################33

#   section 2 

#  difference between list and tuple
#   list = [1,2,3,4,5,6,7]    mutable
#   tuple = (1,2,3,4,5,6,7)    immutable

#  shallow copy deep copy difference
# shallow copy just copies and can change but deepcopy is copied and never changes
# lst = [1,2,3,4]
# a = lst.copy()
# lst.append(5)
# a.append(5)
# print(a)
# print(lst)


#  closures
# closures just work inside one function 

# def outer(x):
#     def inner(y):
#         return x + y
#     return inner
# closure = outer(5)
# print(closure(2))

# function using args and sum
# def outer():
#     def inner(*args):
#         return sum(args)
#     return inner

# closure = outer()
# print(closure(1,2,3,4,5,6))

#  output is 15

#################33
# section 3

# def convert_to_float(lst):
#     new = []
#     for s in lst:
#         float_num = float(s)
#         new.append(float_num)
#     return new

# print(convert_to_float(["1", "2.5", "3"]))

# vowel count

# def count_vowel(string):
#     count = 0
#     list = []
#     vowels = "aeuioAEUIO"
#     for char in string:
#         if char in vowels:
#             list.append(char)
#             count += 1
#     new = list[::-1]
#     return f"The number of vowels is {count}. The reversed is {new}"

# print(count_vowel("hello world"))

### dict method

# def unique_values(dict_list):
#     new = []
#     for dict in dict_list:
#         for value in dict.values():
#             if value not in new:
#                 new.append(value)
#     sorted = set(new)
#     return sorted

# dict_list = [{"a": 1, "b": 2}, {"b": 3, "c": 2}]
# print(unique_values(dict_list))  # Output: {1, 2, 3}


#   fibonacci generator
# 0 1 1 2 3 5 8 13
# def fibonacci_gen(n):
#     first = 0
#     second = 1
#     for i in range(n):
#         first = first + second
#         second = first 
#         yield i

# for num in fibonacci_gen(5):
#     print(num)

#   timer decorator
# import time
# def timer_decorator():
#     def inner():
#         start = time.time()
#         for num in range(1, 1000000):
#             result = sum(num)
#         end = time.time()
#         print(f"Execution time is {end - start} seconds")
#         return result
#     return inner

# @timer_decorator


#   advanced problem


# def sort_tuple(lst):
#     new = []
#     for m in lst:
#         for i in m:
#             if i is int:
#               new.append(i)
#     sorted = new.sort()
#     return sorted

# data = [("apple", 5), ("banana", 2), ("cherry", 8)]
# print(sort_tuple(data))


#################33


# exam review 

#   set add we use add() function not inser() 


# import copy

# # Shallow copy
# lst1 = [[1, 2], [3, 4]]
# shallow_copy = copy.copy(lst1)
# shallow_copy[0][0] = 10
# print(lst1)  # Output: [[10, 2], [3, 4]] (nested list changed)

# # Deep copy
# deep_copy = copy.deepcopy(lst1)
# deep_copy[0][0] = 20
# print(lst1)  # Output: [[10, 2], [3, 4]] (original list unchanged)
# print(deep_copy)  # Output: [[20, 2], [3, 4]] (deep copy changed)

########################3

# def sum_args(*args):
#     return sum(args)

# print(sum_args(1, 2, 3, 4))  # Output: 10

########################

# def convert_to_float(lst):
#     return [float(i) for i in lst]

# print(convert_to_float(["1", "2.5", "3"]))  # Output: [1.0, 2.5, 3.0]


############################33


# def count_vowel(string):
#     vowels = "aeuioAEUIO"
#     vowel_list = [char for char in string if char in vowels]
#     return f"Vowels in reverse order: {vowel_list[::-1]}"

# print(count_vowel("hello world"))  # Output: Vowels in reverse order: ['o', 'o', 'e']

########################3

# def unique_values(dict_list):
#     values = set()
#     for d in dict_list:
#         values.update(d.values())
#     return values

# dict_list = [{"a": 1, "b": 2}, {"b": 3, "c": 2}]
# print(unique_values(dict_list))  # Output: {1, 2, 3}

################################3
# fib generator 

# def fib(n):
#     a,b = 0,1
#     for _ in range(n):
#         yield a
#         a,b = b, a+b
# for num in fib(15):
#     print(num)

###################################3

# import time
# def outer(f):
#     def inner(*args, **kw):
#         start = time.time()
#         result = f(*args, **kw)
#         end = time.time()
#         print(f"Execution time: {end - start} seconds")
#         return result
#     return inner
# @outer
# def summ():
#     return sum(range(1, 1000000))
# print(summ())

#########################333


data = [("apple", 5), ("banana", 2), ("cherry", 8)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)







