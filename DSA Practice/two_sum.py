# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         index_num = []
#         for i in range(len(nums)):
#             for j in range(1+i,len(nums)):
#                 if nums[i] + nums[j] == target:
#                     index_num.append(i)
#                     index_num.append(j)
#         return index_num
                  
# n = [4,3,2,6]
# target = 10
# sum = Solution()
# print(sum.twoSum(n,target))

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_map = {}  # Dictionary to store the number and its index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                print(num_map[complement],i)
                return [num_map[complement], i]  # Return indices if complement found
            num_map[num] = i  # Store the index of the current number
            print(f"num_map in now {num_map}")
        return []  # Return empty list if no solution is found

n = [4, 3, 2, 6]
target = 10
sum_solution = Solution()
print(sum_solution.twoSum(n, target))


