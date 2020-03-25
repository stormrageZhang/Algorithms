'''
常见排序算法分两大类：
1）比较类排序：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此也称为非线性时间比较类排序。
2）非比较类排序：不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此也称为线性时间非比较类排序。
又由不同方式实现，细分为10种排序算法：
比较类：冒泡，快速，简单插入，希尔，简单选择，堆，归并。
非比较类：计数，桶，基数。
'''

'''
颜色分类
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ##冒泡排序 
        if n <= 1:
            return nums 
        for i in range(n-1):
            for j in range(n-1-i):
                if nums[j] > nums[j+1]:
                    nums[j],nums[j+1] = nums[j+1],nums[j]

        ##选择排序 
        for i in range(n-1):
            minindex = i   
            for j in range(i+1,n):
                if nums[j] < nums[minindex]:
                    minindex = j
            nums[i],nums[minindex] = nums[minindex],nums[i]    

        ##插入排序
        for i in range(n):
            cur = nums[i]
            if i == 0 :
                continue
            for j in range(i-1,-1,-1):
                if nums[j] >cur:
                    nums[j+1] = nums[j]
                    if j == 0:
                        nums[j] = cur
                else:
                    nums[j+1] = cur 
                    break

        ##希尔排序
        gap = int(n/2)
        while gap > 0:
            for i in range(gap,n):
                temp = nums[i]
                j = i
                while j >= gap and nums[j-gap] > temp:
                    nums[j] = nums[j-gap]
                    j -= gap 
                nums[j] = temp
            gap = int(gap/2)

        ##归并排序
        def merge(arr,l,m,r):
            n1 = m - l + 1
            n2 = r - m 
            L = [0 for _ in range(n1)]
            R = [0 for _ in range(n2)]
            for i in range(n1):
                L[i] = arr[l + i]
            for j in range(n2):
                R[j] = arr[m + 1 + j]
            i,j = 0,0
            k = l 
            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            while i < n1:
                arr[k] = L[i]
                k += 1
                i += 1
            while j < n2:
                arr[k] = R[j]
                k += 1
                j += 1
        def mergeSort(arr,l,r):
            if l < r :
                m = int((l + (r-1))/2)
                mergeSort(arr,l,m)
                mergeSort(arr,m+1,r)
                merge(arr,l,m,r)
        mergeSort(nums,0,n-1)

        ##快速排序
        def partition(arr,l,r):
            i = l - 1
            pivot = arr[r]
            for j in range(l,r):
                if arr[j] <= pivot:
                    i += 1
                    arr[i],arr[j] = arr[j],arr[i]
            arr[i + 1] ,arr[r] = arr[r],arr[i + 1]
            return (i + 1)
        def quickSort(arr,l,r):
            if l < r:
                pi = partition(arr,l,r)
                quickSort(arr,l,pi-1)
                quickSort(arr,pi+1,r)
        quickSort(nums,0,n-1)

        ##计数排序
        dic = {"0":0,"1":0,"2":0}
        for i in range(n):
            dic[str(nums[i])] += 1
        for i in range(n):
            if dic['0'] > 0:
                nums[i] = 0
                dic['0'] -= 1
            elif dic['1'] > 0:
                nums[i] = 1
                dic['1'] -= 1
            else :
                nums[i] = 2 
                dic['2'] -= 1
       