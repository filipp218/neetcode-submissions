import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_heap = [-num for num in stones]
        heapq.heapify(stones_heap)

        while len(stones_heap) > 1:
            max_stone = -heapq.heappop(stones_heap)
            min_stone = -heapq.heappop(stones_heap)
            if max_stone != min_stone:
                val = abs(max_stone - min_stone)
                heapq.heappush(stones_heap, -val)
        return -stones_heap[0] if stones_heap else 0
                


        