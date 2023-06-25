#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


def findPermutation(s):
    n = len(s)
    perm = []
    low, high = 0, n
    
    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        elif ch == 'D':
            perm.append(high)
            high -= 1
    
    perm.append(low)  # or perm.append(high)
    return perm
s = "IDID"
result = findPermutation(s)
print(result)


# ANS2

# In[4]:


def searchMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        value = matrix[row][col]

        if value == target:
            return True
        elif value > target:
            right = mid - 1
        else:
            left = mid + 1

    return False
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 3

result = searchMatrix(matrix, target)
print(result)


# ANS3

# In[8]:


def validMountainArray(arr):
    if len(arr) < 3:
        return False

    i = 0
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        i += 1

    if i == 0 or i == len(arr) - 1:
        return False

    while i + 1 < len(arr) and arr[i] > arr[i + 1]:
        i += 1

    return i == len(arr) - 1
arr1 = [2, 1]
print(validMountainArray(arr1))  # False

arr2 = [3, 5, 5]
print(validMountainArray(arr2))  # False

arr3 = [0, 3, 2, 1]
print(validMountainArray(arr3))  # True


# ANS4

# In[9]:


def findMaxLength(nums):
    max_len = 0
    count = 0
    count_dict = {0: -1}

    for i, num in enumerate(nums):
        if num == 0:
            count -= 1
        else:
            count += 1

        if count in count_dict:
            curr_len = i - count_dict[count]
            max_len = max(max_len, curr_len)
        else:
            count_dict[count] = i

    return max_len
nums = [0, 1]
result = findMaxLength(nums)
print(result)


# ANS5

# In[13]:


def minProductSum(nums1, nums2):
    nums1.sort()
    nums2.sort(reverse=True)
    min_product_sum = 0
    for i in range(len(nums2)):
        min_product_sum += nums1[i] * nums2[i]
    return min_product_sum
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]
result = minProductSum(nums1, nums2)
print(result)


# ANS6

# In[15]:


from collections import defaultdict

def findOriginalArray(changed):
    count_dict = defaultdict(int)
    for num in changed:
        count_dict[num] += 1

    original = []
    for num in changed:
        if num % 2 == 0 and count_dict[num // 2] > 0:
            original.append(num // 2)
            count_dict[num // 2] -= 1
        else:
            return []

    return original
changed = [1, 3, 4, 2, 6, 8]
result = findOriginalArray(changed)
print(result)


# ANS7

# In[16]:


def generateMatrix(n):
    matrix = [[0] * n for _ in range(n)]
    row_start, row_end = 0, n - 1
    col_start, col_end = 0, n - 1
    num = 1

    while num <= n * n:
        for col in range(col_start, col_end + 1):
            matrix[row_start][col] = num
            num += 1
        row_start += 1

        for row in range(row_start, row_end + 1):
            matrix[row][col_end] = num
            num += 1
        col_end -= 1

        for col in range(col_end, col_start - 1, -1):
            matrix[row_end][col] = num
            num += 1
        row_end -= 1

        for row in range(row_end, row_start - 1, -1):
            matrix[row][col_start] = num
            num += 1
        col_start += 1

    return matrix
n = 3
result = generateMatrix(n)
for row in result:
    print(row)


# ANS8

# In[19]:


from collections import defaultdict

def multiply(mat1, mat2):
    m, k, n = len(mat1), len(mat1[0]), len(mat2[0])
    result_dict = defaultdict(int)

    for r1 in range(m):
        for c1 in range(k):
            val1 = mat1[r1][c1]
            if val1 != 0:
                for r2 in range(k):
                    c2 = c1 + r2
                    if c2 < n:
                        val2 = mat2[c1][c2]
                        if val2 != 0:
                            product = val1 * val2
                            result_dict[(r1, c2)] += product

    result = [[remat1 = [[1, 0, 0],
        [-1, 0, 3]]
mat2 = [[7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]]
result = multiply(mat1, mat2)
for row in result:
    print(row)
sult_dict[(r, c)] for c in range(n)] for r in range(m)]
    return result


# In[ ]:





# In[ ]:




