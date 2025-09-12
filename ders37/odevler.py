# Odev1

# https://leetcode.com/problems/add-two-numbers/description/










# Odev2
nums = [1,2,3,4]
result = []
for i in range(len(nums)):
    temp = 1
    for j in range(len(nums)):
        if i == j:
            continue
        else:
            temp *= nums[j]
    result.append(temp)

print(result)

# Bu soruyu verilen sartlara uygun yapmaya calisiniz
# https://leetcode.com/problems/product-of-array-except-self/description/