class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums1, nums2):
            ret = [0] * (len(nums1) + len(nums2))
            i1 = i2 = ir = 0

            while (i1 < len(nums1) and i2 < len(nums2)):
                if nums1[i1] < nums2[i2]:
                    ret[ir] = nums1[i1]
                    i1 += 1
                else:
                    ret[ir] = nums2[i2]
                    i2 +=1 
                ir +=1
            
            while i1 < len(nums1):
                ret[ir] = nums1[i1]
                i1 +=1
                ir += 1
            
            while i2 < len(nums2):
                ret[ir] = nums2[i2]
                i2 +=1
                ir +=1
            return ret

        
        def mergeSort(arr):
            if len(arr) <= 1:
                return arr

            m = int(len(arr)/ 2)
            l = arr[:m]
            r = arr[m:]
            
            if len(l) > 1:
                l = mergeSort(l)
            
            if len(r) > 1:
                r = mergeSort(r)

            return merge(l,r)


        return mergeSort(nums)