class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def helper(nums: List[int], start: int, end: int, target: int) -> int:
            if end == start:
                if nums[start] == target:
                    return start
                else:
                    return -1
            mid = int((end + start) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return helper(nums, mid + 1, end, target)
            else:
               return helper(nums, start, mid, target)
                
        return helper(nums, 0, len(nums) - 1, target)
