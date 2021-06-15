from typing import List


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    """Finding a sub-array with length less equal to "k", with maximal sum. Then return that sum"""
    if not nums:
        raise ValueError("List is empty!")
    result = 0
    for sub_array_length in range(0, k + 1):
        for index, value in enumerate(nums):
            try:
                if result < sum(nums[index: (index + sub_array_length)]):
                    result = sum(nums[index: (index + sub_array_length)])
                    sub_array = nums[index: (index + sub_array_length)]
            except IndexError:
                break
    return result
