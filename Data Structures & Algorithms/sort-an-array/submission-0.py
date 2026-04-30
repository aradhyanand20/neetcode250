
import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        nums[:] = [heapq.heappop(nums) for _ in range(len(nums))]
        return nums
        