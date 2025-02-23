class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        count = 0
        for i1 in range(m, len(nums1)):
            nums1[i1] = nums2[count]
            count += 1
        nums1.sort()
            
            

solution = Solution()
solution.merge( nums1=[4,5,6,0,0,0], m= 3, nums2=[1,2,3], n=3)

        