#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]

            if abs(curr_sum - target) < abs(closest_sum - target):
                closest_sum = curr_sum

            if curr_sum < target:
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return target

    return closest_sum
nums = [-1, 2, 1, -4]
target = 1
result = threeSumClosest(nums, target)
print(result)


# ANS2

# In[2]:


def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                curr_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if curr_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif curr_sum < target:
                    left += 1
                else:
                    right -= 1

    return result
nums = [1, 0, -1, 0, -2, 2]
target = 0
result = fourSum(nums, target)
print(result)


# ANS3

# In[3]:


def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first decreasing pair from right to left
    while i >= 0 and nums[i] >= nums[i+1]:
        i -= 1

    if i >= 0:
        # Find the smallest element in the suffix that is greater than nums[i]
        j = n - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the suffix nums[i+1:]
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)


# ANS4

# In[4]:


def FindIndex(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
arr = [1,3,5,6] 
target = 5
result = FindIndex(arr,target)
print(result)


# In[5]:


def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)

        
        


# ANS5

# In[7]:


def Add_one_at_last(arr):
    string  = ''.join(str(arr) for array in arr)
    add = string+1
    result = add.split()
    return result

arr = [1,2,3]
sub = Add_one_at_last(arr)
print(sub)


# ANS6

# In[1]:


def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Test the function with the given example
nums = [2, 2, 1]
print(singleNumber(nums))  # Output: 1


# ANS7

# In[2]:


def findMissingRanges(nums, lower, upper):
    ranges = []
    start = lower

    for num in nums:
        if num == start:
            start += 1
        elif num > start:
            if start == num - 1:
                ranges.append([start, start])
            else:
                ranges.append([start, num - 1])
            start = num + 1

    if start <= upper:
        ranges.append([start, upper])

    return ranges

# Test the function with the given example
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(findMissingRanges(nums, lower, upper))  # Output: [[2,2],[4,49],[51,74],[76,99]]


# ANS8

# In[4]:


def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

# Test the function with the given example
intervals = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals))  


# In[ ]:




