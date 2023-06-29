#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[3]:


def find_common_elements(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] < arr2[p2]:
            p1 += 1
        elif arr2[p2] < arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]

result = find_common_elements(arr1, arr2, arr3)
print(result)


# ANS2

# In[4]:


def find_disjoint_nums(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    diff1 = list(set_nums1 - set_nums2)
    diff2 = list(set_nums2 - set_nums1)

    return [diff1, diff2]
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

result = find_disjoint_nums(nums1, nums2)
print(result)


# ANS3

# In[5]:


def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    result = [[0] * rows for _ in range(columns)]

    for row in range(rows):
        for column in range(columns):
            result[column][row] = matrix[row][column]

    return result
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose(matrix)
print(result)


# ANS4

# In[6]:


def array_pair_sum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += nums[i]

    return max_sum
nums = [1, 4, 3, 2]

result = array_pair_sum(nums)
print(result)


# ANS5

# In[7]:


def arrange_coins(n):
    k = 0
    total = 0

    while total <= n:
        k += 1
        total += k

    return k - 1
n = 5

result = arrange_coins(n)
print(result)


# ANS6

# In[8]:


def sorted_squares(nums):
    result = []

    for num in nums:
        result.append(num * num)

    result.sort()

    return result
nums = [-4, -1, 0, 3, 10]

result = sorted_squares(nums)
print(result)


# ANS7

# In[9]:


def max_count(m, n, ops):
    min_row = m
    min_col = n

    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])

    if min_row == m or min_col == n:
        return 0

    return min_row * min_col
m = 3
n = 3
ops = [[2, 2], [3, 3]]

result = max_count(m, n, ops)
print(result)


# ANS8

# In[10]:


def rearrange_array(nums, n):
    result = []

    for i in range(n):
        result.append(nums[i])
        result.append(nums[i+n])

    return result
nums = [2, 5, 1, 3, 4, 7]
n = 3

result = rearrange_array(nums, n)
print(result)


# In[ ]:




