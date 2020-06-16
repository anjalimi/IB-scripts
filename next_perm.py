def nextPermutation(nums):
	numsort = sorted(nums, reverse=True)
	
	if nums == numsort:
		return sorted(nums)

	print nums[2:]+nums[:2]
	# i = len(nums)-1
	# while i:
	# 	if nums[i] > nums[i-1]:
	# 		nums[i],nums[i-1]=nums[i-1],nums[i]
	# 		print nums, "----"
	# 		return nums
	# 	i -= 1

nums = [1,2,3,4]
# nums = [3,2,1]
print nextPermutation(nums)