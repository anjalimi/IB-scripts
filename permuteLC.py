def permute(nums):
    res = []
    if len(nums) == 1:
        res.append(nums)
        return res

    for elem in nums:
        rest = [e for e in nums if e!=elem]
        x = permute(rest)
        for item in x:
            item = item + [elem]
            if item not in res:
                res.append(item)

    return res


nums = [1,2,3]
# nums = [1,2]
print permute(nums)