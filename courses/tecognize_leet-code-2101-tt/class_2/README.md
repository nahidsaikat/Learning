## Topic Discussed:
* Palindrome
* Python OOP (class, object, constructor, attributes, methods)
* Process Control Block (Heap area, stack area, local variables, global variables, data(code))
* Break programming language fear
* Develop mathematical prof of algorithm/solution

### Python OOP

##### Class
A class is a blueprint for the object.
```python
class Parrot:
    pass
```
##### Object
An object has two characteristics:

* attributes
* behavior

Let's take an example:

A parrot is an object, as it has the following properties:

* name, age, color as attributes
* singing, dancing as behavior
```python
class Parrot:

    # class attribute
    species = "bird"

    # instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age

# instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)
```

### Mutable and Immutable in Python
##### Mutable Definition
Mutable is when something is changeable or has the ability to change. In Python, ‘mutable’ is the ability of objects to change their values. These are often the objects that store a collection of data.

##### Immutable Definition
Immutable is the when no change is possible over time. In Python, if the value of an object cannot be changed over time, then it is known as immutable. Once created, the value of these objects is permanent.


### Palindrome
A palindrome is a word, number, phrase, or other sequence of characters which reads the same backward as forward, such as madam or racecar. There are also numeric palindromes, including date/time stamps using short digits 11/11/11 11:11 and long digits 02/02/2020. Sentence-length palindromes ignore capitalization, punctuation, and word boundaries.

```python
s = 'maddam'
start = 0
end = len(s) - 1

while start < end:
    if s[start] != s[end]:
        return False
    start += 1
    end -= 1
return True
```

## Home work
https://leetcode.com/problems/valid-palindrome/
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        s = s.lower()
        
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start] != s[end]:
                return False
            else:
                start += 1
                end -= 1
        return True
```

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] > target:
                end -= 1
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                return [start+1, end+1]
```

### Reading Materials
* https://www.khanacademy.org/computing/ap-computer-science-principles/algorithms-101/evaluating-algorithms/a/verifying-an-algorithm

### References
* https://en.wikipedia.org/wiki/Palindrome
* https://www.programiz.com/python-programming/object-oriented-programming
* https://www.mygreatlearning.com/blog/understanding-mutable-and-immutable-in-python/
