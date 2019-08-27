def maxSubArray(self,A):
        max_end_here = 0
        max_so_far = -100000000          # assumed to be negetive infinity.
        max_sub_array = []
        for i in range(len(A)):
            max_end_here += A[i]
            if max_so_far < max_end_here:
                max_so_far = max_end_here
            if max_end_here < 0:
                max_end_here = 0    
        return max_so_far
