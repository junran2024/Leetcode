
nums=[2,7,11,15]
target = 9

result={}

for i in range(len(nums)):
    if nums[i] in result:
        print(result[nums[i]],i)
        break

    if target-nums[i] not in result:
        result[target-nums[i]]=i
        print(result)
    
    
