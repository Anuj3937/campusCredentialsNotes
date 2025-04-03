# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
# arr = [64, 34, 25, 12, 22, 11, 90]
# print("Before sorting: ", arr)
# sorted_arr = bubble_sort(arr)
# print("After sorting: ", sorted_arr)


# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]
#     return arr
# data = [64, 34, 25, 12, 22, 11, 90]
# print("Original array:", data)
# sorted_array = selection_sort(data)
# a=sorted_array[::-1]
# print("Sorted array:", a)


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
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
# arr = eval(input())
# print("Original array:", arr)
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)

# x=10
# def func():
#     global x
#     x=x+5
#     print(x)
# func()
# print(x)

a,*b,c=[1,2,3,4,5]
print(b)