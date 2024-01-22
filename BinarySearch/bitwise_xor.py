class Solution:
    def xorBeauty(self, nums):
        x_or_list = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    or_value = nums[i] | nums[j]
                    and_value = or_value & nums[k]
                    x_or_value = and_value
                    x_or_list.append(x_or_value)
        
        result = x_or_list[0]

        for i in range(1, len(x_or_list)):
            result = result ^ x_or_list[i]

        return result


# sol = Solution()
# res = sol.xorBeauty([15,45,20,2,34,35,5,44,32,30])

print('*********** OR ***********')
print(1 | 0)
print(0 | 0)
print(1 | 1)
print(0 | 1)

print('*********** and ***********')
print(1 & 0)
print(0 & 0)
print(1 & 1)
print(0 & 1)


print('*********** xor ***********')
print(1 ^ 0)
print(0 ^ 0)
print(1 ^ 1)
print(0 ^ 1)