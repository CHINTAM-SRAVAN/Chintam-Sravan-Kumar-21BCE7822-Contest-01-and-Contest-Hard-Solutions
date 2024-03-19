#User function Template for python3

class Solution:
    def productExceptSelf(self, nums, n):
        prefix_product = [1] * n
        suffix_product = [1] * n
        
        # Calculate prefix products
        for i in range(1, n):
            prefix_product[i] = prefix_product[i - 1] * nums[i - 1]
        
        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_product[i] = suffix_product[i + 1] * nums[i + 1]
        
        # Calculate the product array
        result = [0] * n
        for i in range(n):
            result[i] = prefix_product[i] * suffix_product[i]
        
        return result
            
