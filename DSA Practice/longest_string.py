# 2. Longest Substring Without Repeating Characters
# Problem: Given a string s, find the length of the longest substring without repeating characters.
# Example:
# Input: s = "abcabcbb"
# Output: 3 (substring is "abc")
# Constraints: You must solve it in O(n) time.

class Solution:
    def long_string(self,s):
        s_map = ''
        for x in s:
            if x not in s_map:
                s_map += x
            else: 
                break
        return len(s_map)     
    
s = 'abcabcbb3'
s1 = Solution()
print(s1.long_string(s))

class Solution:
    def long_string(self, s):
        char_set = set()  # Set to store unique characters
        left = 0  # Left pointer for the sliding window
        max_len = 0  # To track the maximum length of the substring
        
        for right in range(len(s)):
            # If we find a repeating character, move the left pointer
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1  # Move left pointer to the right
                
            # Add the current character to the set and update max_len
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        
        return max_len

# Example usage
s = 'abcabcbb3'
s1 = Solution()
print(s1.long_string(s))  # Output should be 4, since "abcb" is the longest substring
