"""
二分查找 (Binary Search) 算法介绍
=====================================

一、概念
--------
二分查找是一种在有序数组中查找目标元素的搜索算法。
其核心思想是：将查找区间从中间分割成两部分，
通过比较中间元素与目标元素的大小关系，
不断缩小搜索范围，直到找到目标或确定不存在。

二、算法原理
------------
1. 在有序数组中，首先确定搜索范围的左边界 left 和右边界 right
2. 计算中间位置 mid = (left + right) // 2
3. 比较 arr[mid] 与目标值 target：
   - 若 arr[mid] == target，找到目标，返回下标
   - 若 arr[mid] < target，目标在右半部分，left = mid + 1
   - 若 arr[mid] > target，目标在左半部分，right = mid - 1
4. 重复步骤 2-3，直到 left > right（未找到）

三、时间与空间复杂度
--------------------
- 时间复杂度：O(log n) - 每次将搜索范围缩小一半
- 空间复杂度：O(1) - 原地操作，不需要额外空间

四、代码实现
------------
"""


def binary_search(arr, target):
    """
    二分查找函数
    
    参数:
        arr: 有序数组（升序）
        target: 要查找的目标值
    
    返回:
        目标值的下标，若不存在返回 -1
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # 未找到


def binary_search_left(arr, target):
    """
    查找左边界：返回第一个 >= target 的位置
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return left


def binary_search_right(arr, target):
    """
    查找右边界：返回第一个 > target 的位置
    """
    left, right = 0, len(arr)
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid
    
    return left


# ==================== 示例演示 ====================

if __name__ == "__main__":
    # 示例1：基本二分查找
    print("=" * 50)
    print("示例1：基本二分查找")
    print("=" * 50)
    
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    print(f"有序数组: {arr}")
    
    target = 11
    result = binary_search(arr, target)
    print(f"查找 {target}, 结果: {result}")
    
    target = 8
    result = binary_search(arr, target)
    print(f"查找 {target}, 结果: {result}")
    
    # 示例2：查找左边界
    print("\n" + "=" * 50)
    print("示例2：查找左边界（第一个 >= 目标的位置）")
    print("=" * 50)
    
    arr2 = [1, 2, 2, 2, 3, 4, 5]
    print(f"数组: {arr2}")
    print(f"目标 2 的左边界: {binary_search_left(arr2, 2)}")  # 输出 1
    print(f"目标 2 的右边界: {binary_search_right(arr2, 2)}")  # 输出 4
    
    # 示例3：查找右边界（适用于统计目标出现次数）
    print("\n" + "=" * 50)
    print("示例3：统计目标元素出现次数")
    print("=" * 50)
    
    arr3 = [1, 2, 2, 2, 2, 3, 4, 5, 5, 6]
    target = 2
    left = binary_search_left(arr3, target)
    right = binary_search_right(arr3, target)
    count = right - left
    print(f"数组: {arr3}")
    print(f"元素 {target} 出现次数: {count}")
    
    # 示例4：二分查找的局限性
    print("\n" + "=" * 50)
    print("示例4：使用场景与局限性")
    print("=" * 50)
    print("✓ 适用于：有序数组、单调函数求根")
    print("✗ 不适用于：无序数组、链表（无法快速访问中间元素）")
    
    # 示例5：搜索旋转排序数组
    print("\n" + "=" * 50)
    print("示例5：进阶 - 搜索旋转排序数组")
    print("=" * 50)
    
    def search_rotated(arr, target):
        """在旋转排序数组中查找目标"""
        if not arr:
            return -1
        
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == target:
                return mid
            
            # 判断左半部分是否有序
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # 右半部分有序
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    
    rotated = [4, 5, 6, 7, 0, 1, 2]
    print(f"旋转数组: {rotated}")
    print(f"查找 0: {search_rotated(rotated, 0)}")  # 输出 4
    print(f"查找 3: {search_rotated(rotated, 3)}")  # 输出 -1
