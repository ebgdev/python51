nums = [5,2,3,4]
length = len(nums)
nums.append(1)
nums.insert(0,1)

result = []
prefix = []
postfix = []

k = 1
for i in range(len(nums)-1):
    k *= nums[i]
    prefix.append(k)

t = 1
for i in range(len(nums)-1,0,-1):
    t *= nums[i]
    postfix.append(t)

postfix.reverse()

for i in range(length): # 0,1,2,3
    print(i)
    result.append(prefix[i]*postfix[i+1])


# ---------------------------------
# def productExceptSelf(nums):
#     n = len(nums)
#     answer = [1] * n
#     prefix = 1
#     for i in range(n):
#         answer[i] = prefix
#         prefix *= nums[i]

#     postfix = 1
#     for i in range(n-1, -1, -1):
#         answer[i] *= postfix
#         postfix *= nums[i]

#     return answer

# print(productExceptSelf(nums=[1,2,3,4]))