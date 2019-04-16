class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m,n=len(nums1),len(nums2)
        if m>n:
            nums1,nums2,m,n=nums2,nums1,n,m
        if n==0:
            raise ValueError

        imin=0
        imax=m
        half_len=(m+n+1)/2
        while imin<=imax:
            i= (imin + imax) / 2
            j=half_len-i
            if i<m and nums2[j-1]>nums1[i]:
                imin = i + 1
            elif i>0 and nums1[i-1] >nums2[j]:
                imax= i-1
            else:
                if i==0:
                    max_of_left = nums2[j - 1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i - 1],nums2[j - 1])
                if (m + n) % 2 == 1:
                    return max_of_left
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        def getKthnum(A, B, k):
            lenA = len(A)
            lenB = len(B)
            if lenA > lenB:
                return getKthnum(B, A, k)
            if lenA == 0:
                return B[k - 1]
            if k == 1:
                return min(A[0], B[0])
            pa = min(lenA, int(k / 2))
            pb = k - pa
            if (A[pa - 1] < B[pb - 1]):
                return getKthnum(A[pa:], B, k - pa )
            else:
                return getKthnum(A, B[pb:], k - pb )

        if (len(nums1) + len(nums2)) % 2 == 1:
            return getKthnum(nums1, nums2, int((len(nums1) + len(nums2) + 1) / 2))
        else:
            return 0.5 * (getKthnum(nums1, nums2, (len(nums1) + len(nums2)) / 2) + getKthnum(nums1, nums2, (
            len(nums1) + len(nums2)) / 2 + 1))
