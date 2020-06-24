# 数组（array）

数组的需求围绕几个核心的目标：求和，变换，排列组合子集，最值状态，最值索引等等。

## 目录

|   需求类型   | 简介 | 方法简介 |
| :----------: | :--: | :------: |
|     求和     |      |          |
|     变换     |      |          |
| 排列组合子集 |      |          |
|   最值状态   |      |          |
|   最值索引   |      |          |

-------

### 求和

#### 两数之和

```python
'''
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic ={}
        for ind,num in enumerate(nums):
            if target-num in dic :
                return [dic[target-num],ind]
            dic[num] = ind 
## 使用哈希表（字典），并且减少重复查询的次数，先查询字典中已有的，若没有适配的值，再加入字典中
```

#### 三数之和

```python
'''
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。注意：答案中不可以包含重复的三元组。
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ##边界问题
        if n <3 :
            return ans
        ## 标配排序，初始化结果
        nums.sort()
        ans=[]
        for i in range(n):
            if nums[i] > 0:
                return ans
            if i>0 and nums[i] == nums[i-1]:
                continue
            ##双指针
            L = i+1
            R = n-1
            while L<R:
                if nums[i]+nums[L]+nums[R] == 0 :
                    ans.append([nums[i],nums[L],nums[R]])
                    while (L<R and nums[L] == nums[L+1] ):
                        L += 1
                    while (L<R and nums[R] == nums[R-1]):
                        R -= 1
                    L += 1
                    R -= 1
                elif nums[i]+nums[L]+nums[R] < 0:
                    L += 1
                else:
                    R -= 1
        return ans
## 第一次遇到双指针解决问题，类似需要遍历的问题，先解决边界问题，使用双指针，注意：跳过重复值，指针符合跳过重复值双跳，不符合直接单跳，跳过重复值需要重申指针关系条件，并放在==关系前。
```

#### 四数之和

```python
'''
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？找出所有满足条件且不重复的四元组。注意：答案中不可以包含重复的四元组。
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ##边界问题
        if n < 4 :
            return []
        ##标配排序，初始化结果
        nums.sort()
        ans = []
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            for j in range(i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                Left = j+1
                Right = n-1
                while Left < Right:
                    new = nums[i] + nums[j] + nums[Left] + nums[Right] 
                    if new == target:
                        ans.append([nums[i],nums[j],nums[Left],nums[Right]])
                        while Left<Right and nums[Left] == nums[Left+1]:
                            Left += 1
                        while Left<Right and nums[Right] == nums[Right-1]:
                            Right -= 1
                        Left += 1
                        Right -= 1
                    elif new < target:
                        Left += 1
                    else:
                        Right -= 1
        return ans
## 两个for循环 一个双指针，与三数求和相似，增加了一个for循环确定第二位的数，对于后两位的数选择，使用双指针。
```

#### 最接近的三数之和

```python
'''
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。
'''
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ##边界问题
        if n < 3:
            return None
        ##标配排序，初始化结果
        nums.sort()
        ans = nums[0]+nums[1]+nums[2]-target
        if ans == 0 :
            return target
        for i in range(n-2):
            L = i+1
            R = n-1
            while L<R :
                ans_new = nums[i]+nums[L]+nums[R]-target
                if ans_new == 0 :
                    return target
                if abs(ans) > abs(ans_new):
                    ans = ans_new
                if ans_new <0:
                    L += 1
                else:
                    R -= 1
        return ans + target
## 还是采用双指针的解决方法
```

