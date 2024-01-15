class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        length = len(nums)

        # Arrays for Pre & Postfix
        prefix_products = [1] * length
        postfix_products = [1] * length

        for i in range(1, length):
            prefix_products[i] = prefix_products[i -1] * nums[i - 1]
        
        for i in range(length -2, -1, -1):
            postfix_products[i] = postfix_products[i + 1] * nums[i + 1]

        product_arr  = [prefix_products[i] * postfix_products[i] for i in range(length)]

        return product_arr


        '''
        Someone else's solution which I really liked:
        class Solution:
            def productExceptSelf(self, nums: List[int]) -> List[int]:
                n = len(nums)
                prefix_product = 1
                postfix_product = 1
                result = [0]*n
                for i in range(n):
                    result[i] = prefix_product
                    prefix_product *= nums[i]
                for i in range(n-1,-1,-1):
                    result[i] *= postfix_product
                    postfix_product *= nums[i]
                return result
        '''
        # This solution is a solution however, it's above the time complexity bound O(N^2)
        # This would give me back 2 (in cas pos was 2)
        # def find_prefix(arr, pos):
        #     product = 1
        #     if(pos != 0):
        #         for num in arr[:pos]:
        #             product *=num
        #         return product
        #     else:
        #         return 1
            
        # def find_postfix(arr,pos):
        #     product = 1
        #     if(pos != len(arr)-1):
        #         for num in arr[pos+1:]:
        #             product*=num
        #         return product
        #     else:
        #         return 1

        # i = 0 
        # product_arr = []
        # while(i <= len(nums)-1):
        #     product1 = find_prefix(nums,i)
        #     product2 = find_postfix(nums,i)
        #     product_arr.append(product1 * product2)

        #     i+=1

        # return product_arr
        
