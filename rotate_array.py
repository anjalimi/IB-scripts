nums = [1,2,3,4,5,6,7]
k = 3

# for i in range(0,k):
# 	# print nums[-1], nums[:-1]
# 	nums = [nums[-1]]+nums[:-1]

nums = nums[len(nums)-k:]+nums[:k]