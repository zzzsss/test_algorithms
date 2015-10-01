class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ls = nums1	#list short
        ll = nums2	#list long
        if len(ls) > len(ll):
        	ls,ll = ll,ls
        l_s,l_l = len(ls),len(ll)
        #0.empty
        if l_s==0:
            if l_l%2==0:
                return (ll[l_l/2]+ll[l_l/2-1])/2.0
            else:
                return ll[(l_l-1)/2]
        #1.short is 1
        if l_s==1:
            #1.1 long is even
            if l_l%2==0:
                if ls[0] < ll[l_l/2-1]:
                    return ll[l_l/2-1]
                if ls[0] > ll[l_l/2]:
                    return ll[l_l/2]
                return ls[0]
            #1.2 long is 1
            elif l_l==1:
                return (ll[0]+ls[0])/2.0
            #1.3 long is odd and >1
            else:
                mid = (l_l-1)/2
                if ls[0] < ll[mid-1]:
                    return (ll[mid]+ll[mid-1])/2.0
                if ls[0] > ll[mid+1]:
                    return (ll[mid]+ll[mid+1])/2.0
                return (ll[mid]+ls[0])/2.0
        #2.short is 2
        elif l_s==2:
            #2.1 long is 2
            if l_l==2:
                tmp = sorted(ls+ll)
                return (tmp[1]+tmp[2])/2.0
            #2.2 long is even
            elif l_l%2==0:
                tmp = sorted(ls+ll[l_l/2-2:l_l/2+2])
                return (tmp[2]+tmp[3])/2.0
            #2.3 odd
            else:
                tmp = sorted(ls+ll[(l_l-3)/2:(l_l+3)/2])
                return tmp[2]
        #3.short is odd
        elif l_s%2==1:
            #3.1 long is odd
            if l_l%2==1:
                mid_s = (l_s-1)/2
                mid_l = (l_l-1)/2
                if ls[mid_s] == ll[mid_l]:
                    return ls[mid_s]
                elif ls[mid_s] > ll[mid_l]:
                    return self.findMedianSortedArrays(ls[0:mid_s+1],ll[mid_s:])
                else:
                    return self.findMedianSortedArrays(ls[mid_s:],ll[0:l_l-mid_s])
            #3.2 long is even
            else:
                mid_s = (l_s-1)/2
                mid_l = (l_l)/2
                if ls[mid_s] > ll[mid_l]:
                    return self.findMedianSortedArrays(ls[0:mid_s+1],ll[mid_s:])    
                elif ls[mid_s] < ll[mid_l-1]:
                    return self.findMedianSortedArrays(ls[mid_s:],ll[0:l_l-mid_s])
                else:
                    return ls[mid_s]
        #4.short is even
        else:
            #4.1 long is odd
            if l_l%2==1:
                mid_s = (l_s)/2
                mid_l = (l_l-1)/2
                if ls[mid_s-1] > ll[mid_l]:
                    return self.findMedianSortedArrays(ls[0:mid_s],ll[mid_s:])
                elif ls[mid_s] < ll[mid_l]:
                    return self.findMedianSortedArrays(ls[mid_s:],ll[0:l_l-mid_s])
                else:
                    return ll[mid_l]
            #4.2 long is even
            else:
                mid_s = l_s/2
                mid_l = l_l/2
                if ls[mid_s-1] >= ll[mid_l-1] and ls[mid_s] <= ll[mid_l]:
                    return (ls[mid_s-1]+ls[mid_s])/2.0
                elif ls[mid_s-1] <= ll[mid_l-1] and ls[mid_s] >= ll[mid_l]:
                    return (ll[mid_l-1]+ll[mid_l])/2.0
                elif ls[mid_s] > ll[mid_l]:
                    return self.findMedianSortedArrays(ls[0:mid_s],ll[mid_s:])
                else:
                    return self.findMedianSortedArrays(ls[mid_s:],ll[0:l_l-mid_s])

