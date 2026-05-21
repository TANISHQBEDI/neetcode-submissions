class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.arr, num)
        self.n += 1

    def findMedian(self) -> float:
        cp = self.arr[:]

        if self.n % 2 == 1:
            for _ in range(self.n // 2 + 1):
                val = heapq.heappop(cp)
            return val

        else:
            for _ in range(self.n // 2 - 1):
                heapq.heappop(cp)

            a = heapq.heappop(cp)
            b = heapq.heappop(cp)

            return (a + b) / 2
"""
[1]
1.0
[1, 3]
2.0
[1, 3, 2]
"""
        