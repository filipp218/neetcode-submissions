class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_border = 0
        right_border = len(heights) - 1
        max_bar = 0
        while left_border < right_border:
            left_height = heights[left_border]
            right_height = heights[right_border]
            min_height = min(left_height, right_height)
            max_bar = max(max_bar, min_height * (right_border - left_border))
            if left_height <= right_height:
                left_border += 1
            else:
                right_border -= 1
        
        return max_bar
        