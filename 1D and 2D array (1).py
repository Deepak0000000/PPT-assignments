#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[11]:


def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for i in range(len(s)):
        if s[i] in s_to_t:
            if s_to_t[s[i]] != t[i]:
                return False
        else:
            s_to_t[s[i]] = t[i]

        if t[i] in t_to_s:
            if t_to_s[t[i]] != s[i]:
                return False
        else:
            t_to_s[t[i]] = s[i]

    return True
s = "egg"
t = "add"
result = isIsomorphic(s, t)
print(result)


# ANS2

# In[12]:


def isStrobogrammatic(num):
    strobogrammatic_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1

    while left <= right:
        if num[left] not in strobogrammatic_pairs or num[right] != strobogrammatic_pairs[num[left]]:
            return False
        left += 1
        right -= 1

    return True
num = "69"
result = isStrobogrammatic(num)
print(result)


# ANS3

# In[13]:


def addStrings(num1, num2):
    i, j = len(num1) - 1, len(num2) - 1
    carry = 0
    result = ""

    while i >= 0 or j >= 0:
        digit1 = int(num1[i]) if i >= 0 else 0
        digit2 = int(num2[j]) if j >= 0 else 0

        temp = digit1 + digit2 + carry
        digit_sum = temp % 10
        carry = temp // 10

        result += str(digit_sum)

        i -= 1
        j -= 1

    if carry > 0:
        result += str(carry)

    return result[::-1]
num1 = "11"
num2 = "123"
result = addStrings(num1, num2)
print(result)


# ANS4

# In[14]:


def reverseWords(s):
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)
s = "Let's take LeetCode contest"
result = reverseWords(s)
print(result)


# ANS5

# In[15]:


def reverseStr(s, k):
    
    s = list(s)
    n = len(s)

    for i in range(0, n, 2 * k):
      
        if i + k <= n:
            s[i:i+k] = s[i:i+k][::-1]
        
        else:
            s[i:] = s[i:][::-1]

    
    return ''.join(s)
s = "abcdefg"
k = 2
result = reverseStr(s, k)
print(result)


# ANS6

# In[16]:


def rotateString(s, goal):
    if len(s) != len(goal):
        return False
    return goal in s + s
s = "abcde"
goal = "cdeab"
result = rotateString(s, goal)
print(result)


# ANS7

# In[17]:


def backspaceCompare(s, t):
    def process_string(string):
        stack = []
        for char in string:
            if char != '#':
                stack.append(char)
            elif stack:
                stack.pop()
        return ''.join(stack)

    return process_string(s) == process_string(t)
s = "ab#c"
t = "ad#c"
result = backspaceCompare(s, t)
print(result)


# ANS8

# In[18]:


def checkStraightLine(coordinates):
    if len(coordinates) <= 2:
        return True

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    slope = (y1 - y0) / (x1 - x0)

   
    for i in range(2, len(coordinates)):
        xi, yi = coordinates[i]
        if (yi - y0) / (xi - x0) != slope:
            return False

    return True
coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
result = checkStraightLine(coordinates)
print(result)


# In[ ]:




