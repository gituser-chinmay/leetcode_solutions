def twoSum(nums, target):
    hm = {}
    for i, v in enumerate(nums):
        if v in hm:
            return [hm[v], i]
        else:
            hm[target - v] = i

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    print(twoSum(nums,target))