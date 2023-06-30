#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


def construct2DArray(original, m, n):
    if m * n != len(original):
        return []  

    result = [[0] * n for _ in range(m)]  
    for i in range(len(original)):
        row = i // n  
        col = i % n  
        result[row][col] = original[i]  

    return result
original = [1, 2, 3, 4, 5, 6]
m = 2
n = 3
result = construct2DArray(original, m, n)
print(result)


# ANS2

# In[2]:


def arrangeCoins(n):
    k = 0  # Number of complete rows
    while n >= k + 1:
        k += 1
        n -= k

    return k
n = 8
result = arrangeCoins(n)
print(result)


# ANS3

# In[3]:


def sortedSquares(nums):
    squared_nums = [num**2 for num in nums]  
    squared_nums.sort()  
    return squared_nums
nums = [-4, -1, 0, 3, 10]
result = sortedSquares(nums)
print(result)


# ANS4

# In[4]:


def findDisjoint(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)  

    distinct_nums1 = list(set1 - set2)  
    distinct_nums2 = list(set2 - set1)  

    return [distinct_nums1, distinct_nums2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisjoint(nums1, nums2)
print(result)


# ANS5

# In[5]:


def distanceValue(arr1, arr2, d):
    distance = 0  
    for num1 in arr1:
        found = False 

        for num2 in arr2:
            if abs(num1 - num2) <= d:
                found = True
                break

        if not found:
            distance += 1

    return distance
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisjoint(nums1, nums2)
print(result)


# ANS6

# In[6]:


def findDuplicates(nums):
    duplicates = []

    for num in nums:
        index = abs(num) - 1
        if nums[index] < 0:
            duplicates.append(index + 1)
        else:
            nums[index] = -nums[index]

    return duplicates
nums = [4, 3, 2, 7, 8, 2, 3, 1]
result = findDuplicates(nums)
print(result)


# ANS7

# In[8]:


def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < nums[mid - 1]:
            return nums[mid]
nums = [3, 4, 5, 1, 2]
result = findMin(nums)
print(result)

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid - 1

   
    return nums[0]
nums = [3, 4, 5, 1, 2]
result = findMin(nums)
print(result)


# ANS8

# In[10]:


from collections import defaultdict

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []  

    freq_map = defaultdict(int)
    for num in changed:
        freq_map[num] += 1

    original = []
    for num in sorted(changed):
        if freq_map[num] == 0:
            continue

        if freq_map[num * 2] == 0:
            return [] 

        original.append(num)
        freq_map[num] -= 1
        freq_map[num * 2] -= 1

    return original
changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)


# In[ ]:




