
# #     Data structures and algorithms


# ###############################################3
# #            Bubble sort 
# #    take one element and compare it with next and if it is higher then swap them until the highest value goes to the last part

# import random
# import time

# # Create a dataset with 10 million random integers
# large_dataset_10M = random.sample(range(1, 10001), 10000)

# # Bubble sort function
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):  # Outer loop runs 'n' times
#         for j in range(0, n-i-1):  # Inner loop runs 'n-i-1' times
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap
        
#     return arr

# # Start the timer for Bubble Sort
# start_time = time.time()
# sorted_dataset_bubble = bubble_sort(large_dataset_10M)
# end_time = time.time()
# bubble_sort_time = end_time - start_time

# # Print the time taken for Bubble Sort
# print(f"\nTime taken to sort the 10 thousand elements using Bubble Sort: {bubble_sort_time} seconds")

# # #####################################################

# #              Merge sort function
# #  so divide the whole set into many subsets until one array has more than one element and merge them together so higher value comes last and do this till all subsets disappear

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]

#     left_half = merge_sort(left_half)
#     right_half = merge_sort(right_half)

#     return merge(left_half, right_half)

# def merge(left, right):
#     result = []
#     i = j = 0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1

#     result.extend(left[i:])
#     result.extend(right[j:])

#     return result

# # Start the timer for Merge Sort
# start_time = time.time()
# sorted_dataset_merge = merge_sort(large_dataset_10M)
# end_time = time.time()
# merge_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Merge Sort: {merge_sort_time} seconds")



# ############################################################

# #           Quick sort
# #    Choose one element as pivot and move it on the left so higher values are on the right then swap pivot element with higher value and do the same until set is correct

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)


# start_time = time.time()
# sorted_quick = quick_sort(large_dataset_10M)
# end_time = time.time()
# quick_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Quick Sort: {quick_sort_time} seconds")


# ###################################################

# #               Selection sort
# #   go through array wholly till u find lowest value and move it to the front of the row and do same until set is correct

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr

# start_time = time.time()
# sorted_selection = selection_sort(large_dataset_10M)
# end_time = time.time()
# selection_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Selection Sort: {selection_sort_time} seconds")


# ##########################################################3

# #         Insertion  sort
# #   takes one element from unsorted part of array and moves it till it finds its correct position so whole set becomes correct till end

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1

#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j] 
#             j -= 1
#         arr[j + 1] = key

#     return arr

# start_time = time.time()
# sorted_inserted = insertion_sort(large_dataset_10M)
# end_time = time.time()
# insertion_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Insertion Sort: {insertion_sort_time} seconds")



# ###############################################################


# #          Heap sort
# #     so apply heapify function so max heap comes to first on set then swap max with last element and reduce heap size by one call heapify again do same until set is sorted

# def heap_sort(arr):
#     def heapify(arr, n, i):
#         largest = i
#         left = 2 * i + 1
#         right = 2 * i + 2
#         if left < n and arr[left] > arr[largest]:
#             largest = left
#         if right < n and arr[right] > arr[largest]:
#             largest = right
#         if largest != i:
#             arr[i], arr[largest] = arr[largest], arr[i]
#             heapify(arr, n, largest)
    
#     n = len(arr)
#     for i in range(n // 2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)

# start_time = time.time()
# sorted_heap = heap_sort(large_dataset_10M)
# end_time = time.time()
# heap_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Heap Sort: {heap_sort_time} seconds")



# #####################################################

# #    Counting sort
# #    find the range of data and create a count array compute the cumulative count and build the sorted output

# def counting_sort1(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)
#     for num in arr:
#         count[num] += 1
#     output = []
#     for i in range(len(count)):
#         output.extend([i] * count[i])
#     return output

 
# start_time = time.time()
# sorted_count = counting_sort1(large_dataset_10M)
# end_time = time.time()
# counting_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Counting Sort: {counting_sort_time} seconds")   




# ##             Radix sort
# #   takes all first digits of all numbers and change in least significant digit order and do the same for tenth and etc nth digit until they become sorted

# def counting_sort(arr, exp):
#     """
#     A function to perform counting sort on the array based on the digit represented by exp (1s, 10s, 100s, etc.)
#     arr: The input array to be sorted.
#     exp: The current digit position (1 for units, 10 for tens, 100 for hundreds, etc.)
#     """
#     n = len(arr)
#     output = [0] * n  # Output array to store sorted numbers.
#     count = [0] * 10  # Count array to store frequency of digits (0 to 9).

#     # Count the occurrences of each digit in the input array.
#     for i in range(n):
#         index = (arr[i] // exp) % 10  # Get the digit at the current place value.
#         count[index] += 1

#     # Update count[i] to store the actual position of the digit in output array.
#     for i in range(1, 10):
#         count[i] += count[i - 1]

#     # Build the output array using the count positions.
#     for i in range(n - 1, -1, -1):  # Traverse the array from end to start to maintain stability.
#         index = (arr[i] // exp) % 10
#         output[count[index] - 1] = arr[i]  # Place the current element in its sorted position.
#         count[index] -= 1

#     # Copy the sorted output array to the original array.
#     for i in range(n):
#         arr[i] = output[i]

# def radix_sort(arr):
#     """
#     A function to implement Radix Sort.
#     arr: The input array to be sorted.
#     """
#     # Find the maximum number to determine the number of digits.
#     max_val = max(arr)

#     # Perform counting sort for every digit. The exp (1s, 10s, 100s, etc.) increases with each pass.
#     exp = 1
#     while max_val // exp > 0:  # Continue until we've sorted by all digit places.
#         counting_sort(arr, exp)  # Sort based on the current digit place.
#         exp *= 10  # Move to the next digit place (10, 100, 1000, etc.)


# start_time = time.time()
# sorted_radix = radix_sort(large_dataset_10M)
# end_time = time.time()
# radix_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Radix Sort: {radix_sort_time} seconds") 



# ####################################################33

# #           Shell sort

# def shell_sort(arr):
#     n = len(arr)
#     gap = n//2
    
#     while gap > 0:
#         for i in range(gap, n):  # Start from the element at index 'gap'
#             temp = arr[i]
#             j = i

#             while j >= gap and arr[j - gap] > temp:
#                 arr[j] = arr[j - gap]
#                 j -= gap

#             arr[j] = temp
#         gap //= 2

#     return arr

# start_time = time.time()
# sorted_shell = shell_sort(large_dataset_10M)
# end_time = time.time()
# shell_sort_time = end_time - start_time
# print(f"\nTime taken to sort the 10 thousand elements using Shell Sort: {shell_sort_time} seconds") 



########################################################3

#              Testing all of them 




# import random
# import time

# # Counting Sort
# def counting_sort(arr):
#     if not arr:
#         return arr

#     min_val = min(arr)
#     max_val = max(arr)
    
#     # Create a count array with the size of the range
#     count = [0] * (max_val - min_val + 1)

#     for num in arr:
#         count[num - min_val] += 1

#     sorted_arr = []
#     for i, count_val in enumerate(count):
#         sorted_arr.extend([i + min_val] * count_val)

#     return sorted_arr

# # Quick Sort (Lomuto Partition Scheme)
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Function to generate large datasets
# def generate_large_dataset(size, max_val):
#     return [random.randint(0, max_val) for _ in range(size)]

# # Function to measure the time taken for sorting
# def measure_time(sort_func, arr):
#     start_time = time.time()
#     sort_func(arr)
#     return time.time() - start_time

# # Define dataset sizes for testing
# sizes = [10**6, 10**7, 10**8]  # 1M, 10M, 100M
# small_range_max = 100  # Small range, 0-100
# large_range_max = 10**9  # Large range, 0-1 billion

# # Test on large datasets
# for size in sizes:
#     print(f"\nSorting dataset of size {size}:")

#     # Small Range Data (0-100)
#     small_range_data = generate_large_dataset(size, small_range_max)
#     counting_sort_time_small = measure_time(counting_sort, small_range_data[:])
#     quick_sort_time_small = measure_time(quick_sort, small_range_data[:])

#     print(f"Small Range Data (0-100):")
#     print(f"Counting Sort Time: {counting_sort_time_small:.6f} seconds")
#     print(f"Quick Sort Time: {quick_sort_time_small:.6f} seconds")

#     # Large Range Data (0-1 billion)
#     large_range_data = generate_large_dataset(size, large_range_max)
#     counting_sort_time_large = measure_time(counting_sort, large_range_data[:])
#     quick_sort_time_large = measure_time(quick_sort, large_range_data[:])

#     print(f"Large Range Data (0-1 Billion):")
#     print(f"Counting Sort Time: {counting_sort_time_large:.6f} seconds")
#     print(f"Quick Sort Time: {quick_sort_time_large:.6f} seconds")



#####################################################

#   Sorted function in python


# import time
# import random

# # Generate random dataset
# def generate_dataset(size):
#     return [random.randint(1, 100000) for _ in range(size)]

# # Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Merge Sort
# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     return merge(left, right)

# def merge(left, right):
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     result.extend(left)
#     result.extend(right)
#     return result

# # Counting Sort
# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for i in range(len(count)):
#         sorted_arr.extend([i] * count[i])
#     return sorted_arr

# # Testing function
# def test_sorting_algorithms(dataset_size):
#     data = generate_dataset(dataset_size)

#     # Timing Quick Sort
#     start_time = time.time()
#     quick_sorted = quick_sort(data.copy())
#     quick_sort_time = time.time() - start_time

#     # Timing Merge Sort
#     start_time = time.time()
#     merge_sorted = merge_sort(data.copy())
#     merge_sort_time = time.time() - start_time

#     # Timing Counting Sort
#     start_time = time.time()
#     counting_sorted = counting_sort(data.copy())
#     counting_sort_time = time.time() - start_time

#     # Timing Python's sorted()
#     start_time = time.time()
#     sorted_data = sorted(data)
#     sorted_time = time.time() - start_time

#     # Print results
#     print(f"Dataset Size: {dataset_size}")
#     print(f"Time taken by Quick Sort: {quick_sort_time:.6f} seconds")
#     print(f"Time taken by Merge Sort: {merge_sort_time:.6f} seconds")
#     print(f"Time taken by Counting Sort: {counting_sort_time:.6f} seconds")
#     print(f"Time taken by sorted() function: {sorted_time:.6f} seconds")
#     print("-" * 50)

# # Run tests with different dataset sizes
# dataset_sizes = [10000, 30000, 50000, 100000]

# for size in dataset_sizes:
#     test_sorting_algorithms(size)


##################################################3

#         Bahtiyorjon sort algorithm

# import random
# import time

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = merge_sort(arr[:mid])
#         right_half = merge_sort(arr[mid:])
        
#         return merge(left_half, right_half)
#     return arr

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for num, freq in enumerate(count):
#         sorted_arr.extend([num] * freq)
#     return sorted_arr

# def hybrid_sort(arr):
#     if len(arr) < 64:
#         return insertion_sort(arr)
    
#     # Detect if it's a small range of integers or sparse data
#     if max(arr) - min(arr) < len(arr):
#         return counting_sort(arr)
    
#     # Otherwise, use Merge Sort
#     return merge_sort(arr)

# # Function to test and compare the performance
# def test_sorting_algorithm(dataset_size):
#     arr = [random.randint(0, 100000) for _ in range(dataset_size)]
    
#     # Timing Hybrid Sort
#     start_time = time.time()
#     hybrid_sort(arr)
#     hybrid_time = time.time() - start_time

#     # Timing TimSort (sorted function)
#     start_time = time.time()
#     sorted(arr)
#     timsort_time = time.time() - start_time
    
#     print(f"Dataset Size: {dataset_size}")
#     print(f"Time taken by TimSort: {timsort_time:.6f} seconds")
#     print(f"Time taken by Hybrid Sort: {hybrid_time:.6f} seconds")
#     print("-" * 50)

# # Test with different dataset sizes
# dataset_sizes = [10000, 30000, 50000, 100000, 1000000, 10000000, 100000000, 500000000]

# for size in dataset_sizes:
#     test_sorting_algorithm(size)


########################################################33

# import random
# import time

# # Insertion Sort
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# # Merge Sort
# def merge_sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         left_half = merge_sort(arr[:mid])
#         right_half = merge_sort(arr[mid:])
#         return merge(left_half, right_half)
#     return arr

# def merge(left, right):
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result

# # Counting Sort
# def counting_sort(arr):
#     max_val = max(arr)
#     count = [0] * (max_val + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for num, freq in enumerate(count):
#         sorted_arr.extend([num] * freq)
#     return sorted_arr

# # Quick Sort
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)

# # Heap Sort
# def heapify(arr, n, i):
#     largest = i
#     l = 2 * i + 1
#     r = 2 * i + 2
#     if l < n and arr[i] < arr[l]:
#         largest = l
#     if r < n and arr[largest] < arr[r]:
#         largest = r
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)

# def heap_sort(arr):
#     n = len(arr)
#     for i in range(n//2 - 1, -1, -1):
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1):
#         arr[i], arr[0] = arr[0], arr[i]
#         heapify(arr, i, 0)
#     return arr

# # Super Hybrid Sort combining all algorithms
# def super_hybrid_sort(arr):
#     if len(arr) < 1000:
#         return insertion_sort(arr)
    
#     # If the range of numbers is small, use Counting Sort
#     if max(arr) - min(arr) < len(arr):
#         return counting_sort(arr)
    
#     # Use Quick Sort for moderately sized arrays
#     if len(arr) < 50000:
#         return quick_sort(arr)
    
#     # Use Merge Sort for large datasets
#     return merge_sort(arr)


# # Test the super hybrid sort against TimSort
# dataset_sizes = [10000, 30000, 50000, 100000, 1000000]
# for size in dataset_sizes:
#     arr = [random.randint(0, 100000) for _ in range(size)]
    
#     # Measure time for Super Hybrid Sort
#     start_time = time.time()
#     super_hybrid_sort(arr.copy())
#     end_time = time.time()
#     hybrid_sort_time = end_time - start_time
    
#     # Measure time for TimSort (using sorted function)
#     start_time = time.time()
#     sorted(arr.copy())
#     end_time = time.time()
#     timsort_time = end_time - start_time
    
#     print(f"Dataset Size: {size}")
#     print(f"Time taken by TimSort: {timsort_time:.6f} seconds")
#     print(f"Time taken by Super Hybrid Sort: {hybrid_sort_time:.6f} seconds")
#     print('-' * 50)




#########################################################

#   Challenge between timsort and counting sort

# import time
# import random

# # TimSort function (Python’s built-in)
# def timsort(arr):
#     return sorted(arr)

# # CountingSort function (for integer arrays within a specific range)
# def counting_sort(arr, max_value):
#     count = [0] * (max_value + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for i in range(max_value + 1):
#         sorted_arr.extend([i] * count[i])
#     return sorted_arr

# # Helper function to test sorting time
# def test_sorting_time(size, sort_func, max_value=None):
#     arr = [random.randint(0, max_value) for _ in range(size)] if max_value is not None else [random.randint(0, 1000) for _ in range(size)]
#     start_time = time.time()
#     # If max_value is provided, pass it along with arr, otherwise just pass the array
#     if max_value is not None:
#         sort_func(arr, max_value)
#     else:
#         sort_func(arr)  # TimSort doesn't need max_value
#     end_time = time.time()
#     return end_time - start_time

# # List of large dataset sizes to test
# sizes = [10, 100, 1000, 5000, 10000, 20000, 50000, 100000, 1000000, 10000000]

# max_value = 1000  # Limiting the range of values for Counting Sort

# # Testing Counting Sort vs TimSort for large datasets
# print("Comparing Counting Sort vs TimSort for large datasets:")
# for size in sizes:
#     # Measure time for Counting Sort (passing max_value)
#     counting_time = test_sorting_time(size, counting_sort, max_value)
#     # Measure time for TimSort (no max_value needed)
#     timsort_time = test_sorting_time(size, timsort)
    
#     print(f"Size: {size} => Counting Sort: {counting_time:.6f}s, TimSort: {timsort_time:.6f}s")


##############################################


#  challenge for count tim and insertion sort

# import time
# import random

# # TimSort function (Python’s built-in)
# def timsort(arr):
#     return sorted(arr)

# # CountingSort function (for integer arrays within a specific range)
# def counting_sort(arr, max_value):
#     count = [0] * (max_value + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_arr = []
#     for i in range(max_value + 1):
#         sorted_arr.extend([i] * count[i])
#     return sorted_arr

# # InsertionSort function
# def insertion_sort(arr):
#     # Iterate over each element in the array starting from the second element
#     for i in range(1, len(arr)):
#         key = arr[i]  # Element to be placed in the sorted part of the array
#         j = i - 1
        
#         # Move elements of arr[0..i-1] that are greater than key to one position ahead
#         while j >= 0 and arr[j] > key:
#             arr[j + 1] = arr[j]
#             j -= 1
        
#         # Insert the key at the correct position
#         arr[j + 1] = key
    
#     return arr

# # Helper function to test sorting time
# def test_sorting_time(size, sort_func, max_value=None):
#     arr = [random.randint(0, max_value) for _ in range(size)] if max_value is not None else [random.randint(0, 1000) for _ in range(size)]
#     start_time = time.time()
#     sort_func(arr, max_value) if max_value is not None else sort_func(arr)  # Pass the array and max_value if needed
#     end_time = time.time()
#     return end_time - start_time

# # List of large dataset sizes to test
# sizes = [10000, 5000, 10, 200]

# max_value = 1000  # Limiting the range of values for Counting Sort

# # Testing Counting Sort, TimSort, and Insertion Sort for large datasets
# print("Comparing Counting Sort vs TimSort vs Insertion Sort for large datasets:")
# for size in sizes:
#     # Measure time for Counting Sort (passing max_value)
#     counting_time = test_sorting_time(size, counting_sort, max_value)
#     # Measure time for TimSort (no max_value needed)
#     timsort_time = test_sorting_time(size, timsort)
#     # Measure time for Insertion Sort
#     insertion_time = test_sorting_time(size, insertion_sort)
    
#     print(f"Size: {size} => Counting Sort: {counting_time:.6f}s, TimSort: {timsort_time:.6f}s, Insertion Sort: {insertion_time:.6f}s")



##################################################################

#    Challenge between timsort counting quick and merge sort


# import time
# import random
# import matplotlib.pyplot as plt

# def timsort(arr):
#     return sorted(arr)

# #############################################################

# def counting_sort(arr):
#     max_value = max(arr)
#     count = [0] * (max_value + 1)
#     for num in arr:
#         count[num] += 1
#     sorted_array = []
#     for num, freq in enumerate(count):
#         sorted_array.extend([num] * freq)
#     return sorted_array

# ##################################################################

# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     left_half = arr[:mid]
#     right_half = arr[mid:]
#     sorted_left = merge_sort(left_half)
#     sorted_right = merge_sort(right_half)
#     return merge(sorted_left, sorted_right)

# def merge(left, right):
#     sorted_array = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             sorted_array.append(left[i])
#             i += 1
#         else:
#             sorted_array.append(right[j])
#             j += 1
#     sorted_array.extend(left[i:])
#     sorted_array.extend(right[j:])
#     return sorted_array

# #####################################################################

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[-1]
#     left = [x for x in arr[:-1] if x <= pivot]
#     right = [x for x in arr[:-1] if x > pivot]
#     sorted_left = quick_sort(left)
#     sorted_right = quick_sort(right)
#     return sorted_left + [pivot] + sorted_right

# #############################################################################

# #   Testing

# dataset_sizes = [1000, 10000, 50000, 100000, 1000000, 5000000]
# algorithms = {
#     "Counting Sort": counting_sort,
#     "Python Built-in": sorted
# }

# results = {name: [] for name in algorithms.keys()}

# for size in dataset_sizes:
#     arr = [random.randint(0, 100000) for _ in range(size)]
#     print(f"\nTesting dataset of size {size}...")
#     for name, sort_func in algorithms.items():
#         print(f"  Running {name}...")
#         test_arr = arr.copy()
#         start_time = time.time()
#         try:
#             sort_func(test_arr)
#             elapsed_time = time.time() - start_time
#             print(f"    Completed {name} in {elapsed_time:.6f} seconds.")
#             results[name].append(elapsed_time)
#         except MemoryError:
#             print(f"    {name} ran out of memory for dataset size {size}.")
#             results[name].append(float('inf'))


# #  plot figures

# plt.figure(figsize=(10, 6))
# for name, times in results.items():
#     plt.plot(dataset_sizes, times, marker='o', label=name)
# plt.title("Sorting Algorithm Performance")
# plt.xlabel("Dataset Size")
# plt.ylabel("Time (seconds)")
# plt.legend()
# plt.grid()
# plt.show()




#########################################################################\


#     Searching Linear search

# import random

# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# arr = [random.randint(0, 1000) for _ in range(1000)]
# target = random.choice(arr)
# result = linear_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")



############################################33


#  Searching 2D array linear search

# import random

# def linear_search_2d(matrix, target):
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if matrix[i][j] == target:
#                 return (i,j)
#     return -1

# matrix = [[random.randint(0,100) for _ in range(100)] for _ in range(10) ]
# target = random.choice(random.choice(matrix))
# result = linear_search_2d(matrix, target)

# # Print the results
# print("Matrix:")
# for row in matrix:
#     print(row)
# print("\nTarget:", target)
# if result != -1:
#     print(f"Target found at position (row {result[0]}, column {result[1]})")
# else:
#     print("Target not found")


###############################################################333

#            Searching binary search

# import random

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# arr = sorted([random.randint(0, 1000) for _ in range(20)])  # Sorted array
# target = random.choice(arr)  # Random target from the array

# print("Sorted Array:", arr)
# print("Target:", target)

# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")



######################################################################33

#        testing time binary interpolation exponential search

# import random
# import time

# # Binary Search
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1

# # Interpolation Search
# def interpolation_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#     while low <= high and target >= arr[low] and target <= arr[high]:
#         pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])
#         if arr[pos] == target:
#             return pos
#         elif arr[pos] < target:
#             low = pos + 1
#         else:
#             high = pos - 1
#     return -1

# # Exponential Search
# def exponential_search(arr, target):
#     if arr[0] == target:
#         return 0
#     index = 1
#     while index < len(arr) and arr[index] < target:
#         index *= 2
#     return binary_search(arr[index // 2: min(index, len(arr))], target)

# # Create a large sorted array for testing
# arr = sorted([random.randint(0, 1000000) for _ in range(100000)])

# # Choose a random target from the array
# target = random.choice(arr)

# # Measure the time taken for each search method

# # Binary Search
# start_time = time.time()
# binary_result = binary_search(arr, target)
# binary_time = time.time() - start_time

# # Interpolation Search
# start_time = time.time()
# interpolation_result = interpolation_search(arr, target)
# interpolation_time = time.time() - start_time

# # Exponential Search
# start_time = time.time()
# exponential_result = exponential_search(arr, target)
# exponential_time = time.time() - start_time

# # Display the results
# print(f"Binary Search Result: {binary_result}, Time Taken: {binary_time:.6f} seconds")
# print(f"Interpolation Search Result: {interpolation_result}, Time Taken: {interpolation_time:.6f} seconds")
# print(f"Exponential Search Result: {exponential_result}, Time Taken: {exponential_time:.6f} seconds")



######################################################################33

#     Linked lists

# import time
# import sys
# sys.setrecursionlimit(1500000) 
# sys.set_int_max_str_digits(1000000)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# start = time.time()
# print(factorial(100))
# end = time.time()

# print(f"Execution time {end - start}")


#########################################


#  Stacks 

# class Stack():
#     def __init__(self):
#         self.stack = []
    
#     def isempty(self):
#         return len(self.stack) == 0

#     def push(self, value):
#         self.stack.append(value)

#     def pop(self):
#         if self.isempty():
#             return "Stack is empty!"
#         return self.stack.pop()

#     def peek(self):
#         if self.isempty():
#             return "Stack is empty!"
#         return self.stack[-1]

#     def size(self):
#         return len(self.stack)


# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)


# print(stack.peek())  # Output: 30
# print(stack.pop())   # Output: 30
# print(stack.size())



###########################################

#  Queues 

# class Queue():
#     def __init__(self):
#         self.queue = []

#     def isempty(self):
#         return len(self.queue) == 0

#     def enqueue(self, value):
#         self.queue.append(value)

#     def dequeue(self):
#         if self.isempty():
#             return "Queue is empty!"
#         return self.queue.pop(0)

#     def size(self):
#         return len(self.queue)

#     def peek(self):
#         if self.isempty():
#             return "Queue is empty!"
#         return self.queue[0]



# queue = Queue()
# queue.enqueue(10)
# queue.enqueue(20)
# queue.enqueue(30)
# print(queue.dequeue())
# print(queue.peek())  # Output: 10
# print(queue.dequeue())  # Output: 10
# print(queue.size())



#################################################

#   Hash tables


# def hash_function(value):
#     sum_of_chars = 0
#     for char in value:
#         sum_of_chars += ord(char)
#     return sum_of_chars % 10

# print("'Bob' has code:", hash_function('Bob'))



########################################################3



#       Projects for 3rd module

#################################################

#   social media feed 

import heapq
import time


class User:
    def __init__(self, username):
        self.username = username

class Post:
    def __init__(self, user, content):
        self.user = user
        self.content = content
        self.timestamp = time.time()
        self.likes = 0
        self.comments = []


    def add_comment(self, comment):
        self.comments.append(comment)

    def like(self):
        self.likes += 1

    def __str__(self):
        return f"Post by {self.user.username}: {self.content} | Likes: {self.likes} | Comments: {len(self.comments)}"









