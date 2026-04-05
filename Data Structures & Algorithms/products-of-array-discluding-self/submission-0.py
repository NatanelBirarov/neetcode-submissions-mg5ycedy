class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProds = [1]
        suffixProds = [1]
        outputs = []

        for i in range(len(nums)):
            prefixProds.append(nums[i] * prefixProds[-1])
        for i in range(len(nums) - 1, -1, -1):
            suffixProds.append(nums[i] * suffixProds[-1])
        print(prefixProds)
        print(suffixProds)
        # arrProd = prefixProds[-1]
        for i in range(len(nums)):
            print(prefixProds[i], suffixProds[len(nums) - i])
            outputs.append(prefixProds[i] * suffixProds[len(nums) - i - 1])
        
        return outputs
    
        