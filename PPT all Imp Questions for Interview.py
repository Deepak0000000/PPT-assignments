#!/usr/bin/env python
# coding: utf-8

# ANS1

# In[1]:


def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

# Example usage
input_string = input("Enter a string: ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# ANS2

# In[3]:


def is_palindrome(string):
  
    string = string.replace(" ", "").lower()
    reversed_string = string[::-1]  
    return string == reversed_string


input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")


# ANS3

# In[4]:


def find_largest_element(lst):
    if len(lst) == 0:
        return None 

    largest = lst[0]  

    for num in lst:
        if num > largest:
            largest = num

    return largest


input_list = [5, 8, 3, 10, 1]
largest_element = find_largest_element(input_list)
print("Largest element:", largest_element)


# ANS4

# In[5]:


def count_elements(lst):
    element_count = {}

    for element in lst:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    return element_count


input_list = [1, 2, 3, 2, 1, 3, 4, 5, 4, 4]
occurrence_count = count_elements(input_list)
print("Element occurrence count:", occurrence_count)


# ANS5

# In[6]:


def find_second_largest(lst):
    if len(lst) < 2:
        return None  

    largest = lst[0]
    second_largest = float('-inf')

    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num

    return second_largest


input_list = [5, 8, 3, 10, 1]
second_largest_number = find_second_largest(input_list)
print("Second largest number:", second_largest_number)


# ANS6

# In[7]:


def remove_duplicates(lst):
    return list(set(lst))

# Example usage
input_list = [1, 2, 3, 2, 1, 3, 4, 5, 4, 4]
unique_list = remove_duplicates(input_list)
print("List with duplicates removed:", unique_list)


# ANS7

# In[8]:


def factorial(n):
    if n < 0:
        return None  
    elif n == 0:
        return 1  
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


input_number = int(input("Enter a number: "))
factorial_result = factorial(input_number)

if factorial_result is not None:
    print("Factorial of", input_number, "is:", factorial_result)
else:
    print("Cannot calculate factorial for negative numbers.")


# ANS8

# In[9]:


def is_prime(n):
    if n < 2:
        return False 

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  

    return True 


input_number = int(input("Enter a number: "))
if is_prime(input_number):
    print(input_number, "is a prime number.")
else:
    print(input_number, "is not a prime number.")


# ANS9

# In[10]:


def sort_list_ascending(lst):
    n = len(lst)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst


input_list = [5, 2, 8, 1, 9, 3]
sorted_list = sort_list_ascending(input_list)
print("Sorted list in ascending order:", sorted_list)


# ANS10

# In[11]:


def sum_of_numbers(lst):
    total = 0
    for number in lst:
        total += number
    return total


input_list = [5, 2, 8, 1, 9, 3]
sum_result = sum_of_numbers(input_list)
print("Sum of numbers:", sum_result)


# ANS11

# In[12]:


def find_common_elements(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print("Common elements:", common_elements)


# ANS12

# In[13]:


def is_anagram(string1, string2):
    
    string1 = string1.lower().replace(" ", "")
    string2 = string2.lower().replace(" ", "")

    if len(string1) != len(string2):
        return False  

    
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    return sorted_string1 == sorted_string2


input_string1 = input("Enter the first string: ")
input_string2 = input("Enter the second string: ")

if is_anagram(input_string1, input_string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# ANS13

# In[14]:


def generate_permutations(string):
    permutations = []

    
    def permute(current_string, remaining_string):
        if len(remaining_string) == 0:
            permutations.append(current_string)
        else:
            for i in range(len(remaining_string)):
                new_current = current_string + remaining_string[i]
                new_remaining = remaining_string[:i] + remaining_string[i+1:]
                permute(new_current, new_remaining)

    permute("", string)
    return permutations


input_string = input("Enter a string: ")
permutations = generate_permutations(input_string)
print("Permutations:")
for permutation in permutations:
    print(permutation)


# ANS14

# In[15]:


def fibonacci_sequence(n):
    sequence = []
    if n <= 0:
        return sequence  
    elif n == 1:
        sequence.append(0)  
    elif n == 2:
        sequence.extend([0, 1])  
    else:
        sequence.extend([0, 1]) 
        while len(sequence) < n:
            next_term = sequence[-1] + sequence[-2]
            sequence.append(next_term)

    return sequence


num_terms = int(input("Enter the number of terms: "))
fib_sequence = fibonacci_sequence(num_terms)
print("Fibonacci sequence up to", num_terms, "terms:", fib_sequence)


# ANS15

# In[16]:


def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    
    if n % 2 == 0:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        median = (mid1 + mid2) / 2
    else:
        median = sorted_numbers[n // 2]
    
    return median


input_numbers = [5, 2, 8, 1, 9, 3]
median = find_median(input_numbers)
print("Median:", median)


# ANS16

# In[1]:


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
my_list = [1, 2, 3, 4, 5]
print(is_sorted(my_list))  

my_list = [1, 3, 2, 4, 5]
print(is_sorted(my_list))  


# ANS17

# In[2]:


def find_intersection(list1, list2):
    intersection = []
    for element in list1:
        if element in list2 and element not in intersection:
            intersection.append(element)
    return intersection



list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

intersection = find_intersection(list1, list2)
print(intersection)  


# ANS18

# In[3]:


def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
my_list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(my_list))  # Output: 6


# ANS19

# In[4]:


def remove_vowels(string):
    vowels = "aeiouAEIOU"
    result = ""
    for char in string:
        if char not in vowels:
            result += char
    return result



input_string = "Hello, World!"
output_string = remove_vowels(input_string)
print(output_string)  


# ANS20

# In[5]:


def reverse_words(sentence):
    words = []
    current_word = ""
    for char in sentence:
        if char == " ":
            if current_word:
                words.append(current_word)
                current_word = ""
        else:
            current_word += char

    if current_word:
        words.append(current_word)

    reversed_sentence = ""
    for i in range(len(words) - 1, -1, -1):
        reversed_sentence += words[i] + " "

    return reversed_sentence.strip()



input_sentence = "Hello, World! How are you?"
output_sentence = reverse_words(input_sentence)
print(output_sentence)  


# ANS21

# In[6]:


def are_anagrams(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    if len(str1) != len(str2):
        return False

    char_count = {}

    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char in str2:
        if char in char_count:
            char_count[char] -= 1
            if char_count[char] == 0:
                del char_count[char]
        else:
            return False

    return len(char_count) == 0



string1 = "listen"
string2 = "silent"
if are_anagrams(string1, string2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")


# ANS22

# In[7]:


def find_first_non_repeating_character(string):
    character_count = {}

    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    for char in string:
        if character_count[char] == 1:
            return char

    return None



input_string = "abracadabra"
output_character = find_first_non_repeating_character(input_string)
if output_character:
    print("The first non-repeating character is:", output_character)
else:
    print("There are no non-repeating characters in the string.")


# ANS23

# In[10]:


def find_prime_factors(number):
    factors = []

   
    while number % 2 == 0:
        factors.append(2)
        number = number // 2

    
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number = number // divisor
        else:
            divisor += 2

    if number > 2:
        factors.append(number)

    return factors



input_number = 84
prime_factors = find_prime_factors(input_number)
print("Prime factors of", input_number, "are:", prime_factors)


# ANS24

# In[11]:


def is_power_of_two(number):
    if number <= 0:
        return False

    while number > 1:
        if number % 2 != 0:
            return False
        number //= 2

    return True



input_number = 16
if is_power_of_two(input_number):
    print(input_number, "is a power of two.")
else:
    print(input_number, "is not a power of two.")


# ANS25

# In[12]:


def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

   
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1

    return merged_list



sorted_list1 = [1, 3, 5, 7]
sorted_list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(sorted_list1, sorted_list2)
print("Merged list:", merged_list)


# ANS26

# In[1]:


def find_mode(numbers):
    
    count_dict = {}
    
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    
    max_count = 0
    mode = []
    for num, count in count_dict.items():
        if count > max_count:
            max_count = count
            mode = [num]
        elif count == max_count:
            mode.append(num)
    
    return mode
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
mode = find_mode(numbers)
print("Mode:", mode)


# ANS27

# In[2]:


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


num1 = 48
num2 = 18
result = gcd(num1, num2)
print("GCD:", result)


# ANS28

# In[4]:


def square_root(number):
    if number < 0:
        raise ValueError("Square root is not defined for negative numbers.")
    
    if number == 0:
        return 0
    
   
    guess = number / 2
    
    
    while True:
        new_guess = (guess + number / guess) / 2
        if abs(new_guess - guess) < 1e-9:  
            break
        guess = new_guess
    
    return new_guess


num = 16
result = square_root(num)
print("Square root:", result)


# ANS29

# In[5]:


import re

def is_valid_palindrome(string):
    
    alphanumeric_string = re.sub(r'\W+', '', string.lower())
    
    
    return alphanumeric_string == alphanumeric_string[::-1]


string1 = "A man, a plan, a canal, Panama!"
print(is_valid_palindrome(string1))  # True

string2 = "Hello, World!"
print(is_valid_palindrome(string2))  # False


# ANS30

# In[6]:


def find_minimum(nums):
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        
        if nums[mid] > nums[right]:
            left = mid + 1
        
        elif nums[mid] < nums[right]:
            right = mid
        
        else:
            right -= 1
    
    
    return nums[left]


nums = [4, 5, 6, 7, 0, 1, 2]
result = find_minimum(nums)
print("Minimum element:", result)


# ANS31

# In[7]:


def sum_even_numbers(numbers):
    total_sum = 0
    
    for num in numbers:
        if num % 2 == 0:
            total_sum += num
    
    return total_sum


num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_even_numbers(num_list)
print("Sum of even numbers:", result)


# ANS32

# In[8]:


def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / (base * power(base, -exponent - 1))


base = 2
exponent = 3
result = power(base, exponent)
print("Result:", result)


# ANS33

# In[9]:


def remove_duplicates(lst):
    seen = set()
    result = []
    
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result


my_list = [3, 5, 2, 2, 5, 1, 1, 4, 4]
result = remove_duplicates(my_list)
print("List with duplicates removed:", result)


# ANS34

# In[10]:


def longest_common_prefix(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


strings = ["flower", "flow", "flight"]
result = longest_common_prefix(strings)
print("Longest common prefix:", result)


# ANS35

# In[11]:


def is_perfect_square(num):
    if num < 0:
        return False
    
    if num == 0:
        return True
    
    guess = num // 2
    
    while guess * guess > num:
        guess = (guess + num // guess) // 2
    
    return guess * guess == num


number = 25
result = is_perfect_square(number)
print("Is a perfect square:", result)


# ANS36

# In[12]:


def calculate_product(numbers):
    product = 1

    for num in numbers:
        product *= num

    return product


my_list = [2, 3, 4, 5]
result = calculate_product(my_list)
print("Product:", result)


# ANS37

# In[13]:


def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence


input_sentence = "Hello, how are you?"
result = reverse_sentence(input_sentence)
print("Reversed sentence:", result)


# ANS38

# In[14]:


def find_missing_number(numbers):
    n = len(numbers) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number


my_list = [1, 2, 3, 5, 6, 7, 8, 9, 10]
result = find_missing_number(my_list)
print("Missing number:", result)


# ANS39

# In[15]:


def sum_of_digits(number):
    digit_sum = 0

    while number > 0:
        digit = number % 10
        digit_sum += digit
        number //= 10

    return digit_sum


num = 12345
result = sum_of_digits(num)
print("Sum of digits:", result)


# ANS40

# In[16]:


def is_valid_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if string[left] != string[right]:
            return False

        left += 1
        right -= 1

    return True


input_string = "level"
result = is_valid_palindrome(input_string)
print("Is a valid palindrome:", result)


# ANS41

# In[17]:


def find_smallest_missing_positive(nums):
    n = len(nums)

    
    for i in range(n):
        while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

  
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    
    return n + 1


my_list = [3, 4, -1, 1]
result = find_smallest_missing_positive(my_list)
print("Smallest missing positive integer:", result)


# ANS42

# In[18]:


def longest_palindrome_substring(string):
    n = len(string)
    start = 0
    max_length = 1

    
    def expand_around_center(left, right):
        while left >= 0 and right < n and string[left] == string[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(n):
        len1 = expand_around_center(i, i)  
        len2 = expand_around_center(i, i + 1)  
        length = max(len1, len2)

        if length > max_length:
            max_length = length
            start = i - (length - 1) // 2

    return string[start:start + max_length]


input_string = "babad"
result = longest_palindrome_substring(input_string)
print("Longest palindrome substring:", result)


# ANS43

# In[19]:


def count_occurrences(numbers, target):
    count = 0

    for num in numbers:
        if num == target:
            count += 1

    return count


my_list = [1, 2, 3, 2, 4, 2, 5]
target_number = 2
result = count_occurrences(my_list, target_number)
print("Number of occurrences:", result)


# ANS44

# In[20]:


def is_perfect_number(number):
    if number <= 0:
        return False

    divisor_sum = 0
    for i in range(1, number):
        if number % i == 0:
            divisor_sum += i

    return divisor_sum == number


num = 28
result = is_perfect_number(num)
print("Is a perfect number:", result)


# ANS45

# In[21]:


def remove_duplicates(string):
    # Convert the string to a list of characters
    chars = list(string)
    
    
    freq = {}
    
   
    for char in chars:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    
    result = []
    
   
    for char in chars:
        if freq[char] == 1:
            result.append(char)
    
   
    return ''.join(result)


input_string = "hello"
result = remove_duplicates(input_string)
print("String after removing duplicates:", result)


# ANS46

# In[22]:


def find_first_missing_positive(nums):
    n = len(nums)

    
    i = 0
    while i < n:
        if 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1

    
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

   
    return n + 1


my_list = [3, 4, -1, 1]
result = find_first_missing_positive(my_list)
print("First missing positive integer:", result)


# In[ ]:




