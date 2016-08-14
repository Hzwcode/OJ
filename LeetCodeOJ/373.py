from heapq import heappush,heappop

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        k_pairs = []
        if len(nums1) > len(nums2):
            tmp = self.kSmallestPairs(nums2, nums1, k)
            for pair in tmp:
                k_pairs.append([pair[1], pair[0]])
            return k_pairs
        else:
            min_heap = []
            def push(i, j):
                if i < len(nums1) and j < len(nums2):
                    heappush(min_heap, [nums1[i] + nums2[j], i, j])
            push(0, 0)
            while min_heap and len(k_pairs) < k:
                _, i, j = heappop(min_heap)
                k_pairs.append([nums1[i], nums2[j]])
                push(i, j+1)
                if j == 0:
                    push(i+1, 0)
            return k_pairs
