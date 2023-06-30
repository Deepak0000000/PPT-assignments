#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[19]:


def minimumDeleteSum(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize base cases
    for i in range(1, m + 1):
        dp[i][0] = dp[i-1][0] + ord(s1[i-1])
    for j in range(1, n + 1):
        dp[0][j] = dp[0][j-1] + ord(s2[j-1])

    # Fill the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

    return dp[m][n]
s1 = "sea"
s2 = "eat"
result = minimumDeleteSum(s1, s2)
print(result)


# ANS2

# In[21]:


def isValid(s):
    stack = []

    for c in s:
        if c == '(' or c == '*':
            stack.append(c)
        elif c == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif stack and stack[-1] == '*':
                stack.pop()
                if stack and stack[-1] == '(':
                    stack.pop()
            else:
                return False

    return not stack
s = "()"
result = isValid(s)
print(result)


# ANS3

# In[22]:


def minSteps(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return (m - dp[m][n]) + (n - dp[m][n])
word1 = "sea"
word2 = "eat"
result = minSteps(word1, word2)
print(result)


# ANS4

# In[24]:


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def constructTree(s):
    if not s:
        return None

    # Find the index of the first open parenthesis '('
    i = s.find('(')

    # Create the current node
    root = TreeNode(int(s[:i]))

    # Find the index of the corresponding closing parenthesis ')'
    j = findClosingParenthesis(s, i)

    # Extract the left subtree string
    left_subtree_str = s[i+1:j]

    # Recursively construct the left subtree
    root.left = constructTree(left_subtree_str)

    # Extract the right subtree string
    right_subtree_str = s[j+1:-1]

    # Recursively construct the right subtree
    root.right = constructTree(right_subtree_str)

    return root

def findClosingParenthesis(s, start):
    count = 0
    for i in range(start, len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                return i
    return -1
s = "4(2(3)(1))(6(5))"
root = constructTree(s)

# Function to traverse the binary tree in-order and return the values as a list
def inorderTraversal(root):
    if not root:
        return []
    return inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)

result = inorderTraversal(root)
print(result)


# ANS5

# In[25]:


def compress(chars):
    write = 0
    count = 1

    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            count += 1
        else:
            chars[write] = chars[i - 1]
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

            count = 1

    chars[write] = chars[-1]
    write += 1

    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1

    return write
chars = ["a", "a", "b", "b", "c", "c", "c"]
new_length = compress(chars)
print(new_length)
print(chars[:new_length])


# ANS6

# In[30]:


def findAnagrams(s, p):
    freq_p = [0] * 26
    freq_window = [0] * 26
    result = []

    for ch in p:
        freq_p[ord(ch) - ord('a')] += 1

    left, right = 0, 0
    while rigs = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)
ht < len(s):
        freq_window[ord(s[right]) - ord('a')] += 1

        if right - left + 1 == len(p):
            if freq_p == freq_window:
                result.append(left)

            freq_window[ord(s[left]) - ord('a')] -= 1
            left += 1

        right += 1

    return result
s = "cbaebabacd"
p = "abc"
result = findAnagrams(s, p)
print(result)


# ANS7

# In[31]:


def decodeString(s):
    stack = []
    curr_str = ""
    curr_num = 0

    for ch in s:
        if ch.isdigit():
            curr_num = curr_num * 10 + int(ch)
        elif ch == "[":
            stack.append((curr_num, curr_str))
            curr_num = 0
            curr_str = ""
        elif ch == "]":
            prev_num, prev_str = stack.pop()
            curr_str = prev_str + curr_str * prev_num
        else:
            curr_str += ch

    return curr_str
s = "3[a]2[bc]"
result = decodeString(s)
print(result)


# ANS8

# In[33]:


def buddyStrings(s, goal):
    if len(s) != len(goal):
        return False

    if s == goal:
        # Check if s contains any repeated characters
        seen = set()
        for s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)
ch in s:
            if ch in seen:
                return True
            seen.add(ch)
        return False

    differences = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            differences.append(i)

    return len(differences) == 2 and s[differences[0]] == goal[differences[1]] and s[differences[1]] == goal[differences[0]]
s = "ab"
goal = "ba"
result = buddyStrings(s, goal)
print(result)


# In[ ]:




