#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[26]:


def two_sum(nums, target):
    # Create a hash map to store the elements and their indices
    num_map = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the hash map
        if complement in num_map:
            # Return the indices of the two numbers
            return [num_map[complement], i]
        
        # Add the current element to the hash map
        num_map[num] = i
    
    # If no solution is found, return an empty list
    return []
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


# ANS2

# In[28]:


def remove_element(nums, val):
    # Initialize two pointers: one for the current position and one for the next position to overwrite
    curr = 0
    next_pos = 0
    
    # Iterate through the array
    while curr < len(nums):
        # If the current element is not equal to val, keep it in the array
        if nums[curr] != val:
            nums[next_pos] = nums[curr]
            next_pos += 1
        
        curr += 1
    
    # Return the count of elements that are not equal to val
    return next_pos
nums = [3, 2, 2, 3]
val = 3
result = remove_element(nums, val)
print(result)  


# ANS3

# In[29]:


def search_index(nums,target):
    left = 0
    right  = len(nums)-1
    
    while left<=right:
        mid  = (left+right)//2
        if mid == target:
            return mid
        if nums[left]<target:
            left = mid+1
        else:
            right = mid-1
            
    return left
nums = [2,3,4,5,6]
target = 3
result = search_index(nums,target)
print(result)
            


# In[30]:


def serach_index(nums,target):
    for i in range(len(nums)):
        if i == target:
            return i
        
nums = [2,3,4,5,6]
target = 3
result = search_index(nums,target)
print(result)
            
        
        


# ANS4

# In[31]:


def addToArrayForm(digits, num):
    # Convert the large integer represented by the digits array to a string and then to an integer
    n = int(''.join(map(str, digits)))
    
    # Add the two numbers and convert the result to an array of digits
    result = list(str(n + num))
    
    # Convert each digit in the result back to an integer
    result = list(map(int, result))
    
    return result
digits = [1, 2, 3]
num = 456
result = addToArrayForm(digits, num)
print(result)  # Output: [1, 6, 7, 9]


# ANS5

# In[32]:


def merge(nums1, m, nums2, n):
    # Initialize pointers for nums1, nums2, and the merged array
    p1 = m - 1
    p2 = n - 1
    p3 = m + n - 1
    
    # Merge the arrays from the end
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p3] = nums1[p1]
            p1 -= 1
        else:
            nums1[p3] = nums2[p2]
            p2 -= 1
        p3 -= 1
    
    # If there are remaining elements in nums2, copy them to nums1
    if p2 >= 0:
        nums1[:p2+1] = nums2[:p2+1]
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]


# ANS6

# In[33]:


def containsDuplicate(nums):
    num_set = set()
    for num in nums:
        if num in num_set:
            return True
        num_set.add(num)
    return False
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True


# ANS7

# In[37]:


def moveZeroes(nums):
    left = 0
    right = 0
    
    while left < len(nums):
        if nums[left] != 0:
            nums[right] = nums[left]
            right += 1
        left += 1
    
    while right < len(nums):
        nums[right] = 0
        right += 1
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True


# ANS8

# In[39]:


def findErrorNums(nums):
    n = len(nums)
    total_sum = n * (n + 1) // 2
    array_sum = sum(nums)
    diff = total_sum - array_sum
    
    num_freq = {}
    duplicate = -1
    
    for num in nums:
        if num in num_freq:
            duplicate = num
        else:
            num_freq[num] = 1
    
    missing = duplicate - diff
    
    return [duplicate, missing]
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)  


# In[ ]:




