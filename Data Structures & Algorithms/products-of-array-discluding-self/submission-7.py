class Solution:
    def zero_element(self, nums: List[int], index) -> int:
        product = 1
        for i, e in enumerate(nums):
            if i != index:
                product *= e
        
        return product

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        another_array = []

        for num in nums:
            product *= num

        for i in range(len(nums)):
            another_array.append(product)

        for index, element in enumerate(another_array):
            if nums[index] != 0:
                another_array[index] = int(another_array[index] / nums[index])
            else:
                another_array[index] = self.zero_element(nums, index)

        return another_array

            