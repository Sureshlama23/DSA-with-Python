# Revese array
# class solution:

#     def reverse(self,num):
#         r = num[::-1]
#         print(r)

# num = [1,3,5,6,9]
# r1 = solutation()
# r1.reverse(num)


# Min and Max find out

# class Solution:
#     def minNmax(self,num_list):
#         if not num_list:
#             return None, None
#         # index = 0, 1, 2 , 3, 4 ,5
#         # value = 2, 5, 1,   6, 9, 7
#         min_num = num_list[0]
#         max_num = num_list[0]
#         for num in num_list[1::]:
#             if num > max_num:
#                 max_num = num
#             if num < min_num:
#                 min_num = num      
#         return min_num, max_num

# num = [2,5,1,6,9,7]
# m1 = Solution()
# min_num, max_num = m1.minNmax(num)
# print(f'min value is: {min_num} max value is {max_num}')
# def find_max_and_min(arr):
#     # Edge case: if the array is empty, return None
#     if not arr:
#         return None, None

#     # Initialize max_element and min_element to the first element of the array
#     max_element = arr[0]
#     min_element = arr[0]

#     # Loop through the array starting from the second element
#     for num in arr[1:]:
#         # Update max_element if num is greater
#         if num > max_element:
#             max_element = num
#         # Update min_element if num is smaller
#         if num < min_element:
#             min_element = num

#     return max_element, min_element

# # Example usage:
# arr = [1, 3, 5, 7, 2]
# max_val, min_val = find_max_and_min(arr)
# print(f"Max = {max_val}, Min = {min_val}")




# 3. Find the Kth Smallest Element in an Array
# Problem: Given an array and a number k, find the kth smallest element in the array.
# Example:
# Input: arr = [7, 10, 4, 3, 20, 15], k = 3
# Output: 7

# def find_kth_smallest(arr,k):
#     if not arr: 
#         return None
#     arr.sort()
#     # Return the k-th smallest element (index k-1)
#     return arr[k-1] if 0 < k <= len(arr) else None 
    
# arr = [7, 10, 4, 3, 20, 15]
# k = 3
# kth_smallest = find_kth_smallest(arr,k)
# print(f'The {k}rd smallest element is: {kth_smallest}')



# 4. Find Missing Number in Array
# Problem: Given an array of size n-1 containing distinct integers in the range from 1 to n, find the missing number.
# Example:
# Input: [1, 2, 4, 5, 6]
# Output: 3

# def Solution(num):
#     if not num:
#         return None
#     m = 1
#     for i in range(len(num)):
#         if num[i] == m:
#             m += 1
#         else:
#             break
        
#     return m
    
# num = [1, 2, 4, 5, 6]
# num = [1,2,3,4,5,6,7,8,9,11]
# s1 = Solution(num)
# print(f'The missing number is: {s1}')


# # Best Practice
# def find_missing_number(arr):
#     n = len(arr) + 1  # The length of the array should be n-1, so n is len(arr) + 1
#     total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
#     arr_sum = sum(arr)  # Sum of the given array
#     print(f'arr sum: {arr_sum}')
#     return total_sum - arr_sum  # The missing number is the difference

# # Example usage:
# # arr = [1, 2, 4, 5, 6]
# arr = [1,2,3,4,5,6,7,8,9,11]

# missing_number = find_missing_number(arr)
# print(f'The missing number is: {missing_number}')

# 5. Move All Zeros to End of Array
# Problem: Given an array, move all zeros present in the array to the end without changing the relative order of non-zero elements.
# Example:
# Input: [0, 1, 9, 8, 0, 2, 7, 0, 6, 0]
# Output: [1, 9, 8, 2, 7, 6, 0, 0, 0, 0]

# def Solution(num):
#     if not num:
#         return None
#     index = 0
#     for i in range(len(num)):
#         if num[i] == 0:
#             n = num.pop(i)
#             num.append(n)
#     return num
       
          
# num = [0, 1, 9, 8, 0, 2, 7, 0, 6, 0]
# s1 = Solution(num)
# print(f'The result is {s1}')

# Best approach
# def move_zeros_to_end(arr):
#     if not arr:
#         return None
#     # Pointer for the position of the next non-zero element
#     non_zero_index = 0

#     # Move non-zero elements to the front
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_index] = arr[i]
#             non_zero_index += 1

#     # Fill remaining positions with zeros
#     for i in range(non_zero_index, len(arr)):
#         arr[i] = 0

#     return arr

# # Example usage:
# arr = [0, 1, 9, 8, 0, 2, 7, 0, 6, 0]
# result = move_zeros_to_end(arr)
# print(f'The result is: {result}')




# 6. Rotate an Array by k Elements
# Problem: Rotate an array to the right by k steps.
# Example:
# Input: arr = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# def rotate_array(arr, k):
#     n = len(arr)
#     print(f'n value is: {n}')
#     k = k % n  # Handle cases where k is greater than the array length
#     print(f'k value is: {k}')
    
#     # Step 1: Reverse the whole array
#     arr.reverse()
#     print(f'1 arr {arr}')
    
#     # Step 2: Reverse the first k elements
#     arr[:k] = reversed(arr[:k])
#     print(f'2 arr is {arr}')
    
#     # Step 3: Reverse the remaining elements
#     arr[k:] = reversed(arr[k:])
#     print(f'3 arr is {arr}')
    
#     return arr

# # Example usage:
# arr = [1, 2, 3, 4, 5]
# k = 2
# result = rotate_array(arr, k)
# print(f'The rotated array is: {result}')
 
 
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

nums = [0,1,2,2,3,0,4,2]
val = 2
s1 = Solution()
k = s1.removeElement(nums,val)
print(f'The length of list {k} remain nums is {nums[:k]}')