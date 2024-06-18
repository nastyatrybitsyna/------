def majorityElement(nums):
    counts = {}
    for num in nums:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = max(counts.values())
    for num, count in counts.items():
        if count == max_count:
            return num

print(majorityElement([3, 2, 3]))        
print(majorityElement([2, 2, 1, 1, 1, 2, 2])) 
