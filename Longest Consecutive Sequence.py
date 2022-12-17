class Solution(object):
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        
        nums = set(nums)
        visited = dict([(x, False) for x in nums])
        max_len = 1
        
        for n in nums:
            if visited[n]:
                continue
                
            l = 1
            visited[n] = True
            n_cpy = n
            
            while n_cpy - 1 in nums:
                if visited[n_cpy - 1]:
                    continue                    
                l += 1
                visited[n_cpy - 1] = True
                n_cpy = n_cpy - 1

            while n + 1 in nums:
                l += 1
                visited[n + 1] = True
                n = n + 1

            max_len = max(max_len, l)
        
        return max_len
