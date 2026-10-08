class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        places_nums2 = dict()
        index = 0
        result = []
        for num in nums2:
            places_nums2.setdefault(num, [])
            places_nums2[num].append(index)
            index += 1
        
        for num in nums1:
            index = places_nums2[num].pop()
            result.append(index)

        return result