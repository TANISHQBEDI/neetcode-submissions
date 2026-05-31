class Solution:
    def binSearch(self, arr: List[int], target: int) -> bool:
        l, r = 0, len(arr) - 1
        while l <= r:
            m = l + (r - l)//2
            if arr[m] == target:
                return True
            elif arr[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if self.binSearch(row, target):
                return True
        return False