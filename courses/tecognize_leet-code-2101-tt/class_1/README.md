## Topic Discussed:
* Array/List basics - defining, append and pop method
* Complexity - Time & Space
* List example problem - observe complexity
* Reverse a list with O(n) space complexity
* Reverse a list with O(1) space complexity
* Find a target value in a list

### Home work
https://leetcode.com/problems/two-sum/
#### Solution
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index in range(0, len(nums)-1):
            for index_2 in range(index+1, len(nums)):
                if nums[index] + nums[index_2] == target:
                    return [index, index_2]
```

### Screen shots of hand notes:

List Definition:
![List Definition](https://raw.githubusercontent.com/nahidsaikat/Learning/master/courses/tecognize_leet-code-2101-tt/class_1/images/IMG_20210717_184133.jpg)

Complexity:
![Complexity](https://raw.githubusercontent.com/nahidsaikat/Learning/master/courses/tecognize_leet-code-2101-tt/class_1/images/IMG_20210717_184110.jpg)


O(n) Space Complexity:
![O(n) Space Complexity](https://raw.githubusercontent.com/nahidsaikat/Learning/master/courses/tecognize_leet-code-2101-tt/class_1/images/IMG_20210717_184048.jpg)


O(1) Space Complexity:
![O(1) Space Complexity](https://raw.githubusercontent.com/nahidsaikat/Learning/master/courses/tecognize_leet-code-2101-tt/class_1/images/IMG_20210717_183945.jpg)
