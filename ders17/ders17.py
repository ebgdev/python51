# lst = ['apple', 'banana', 'kiwi', 'apple', 'kiwi', 'orange','apple']

# # output : {'apple':3, 'banana':1 ,}

# def group_by_name(lst):
#     result = {}
#     for item in lst:
#         if item not in result:
#             result[item] = 0
#         result[item]+=1
#     return result

# print(group_by_name(lst))

# -----------------------------------------



# -------------loop-list------------
# nums = [7,3,11,15,6]
# target = 9

# for i in range(0,len(nums)-1): # i = 1
#     for j in range(i+1,len(nums)): # j = 2 , 4 
#         if nums[i] + nums[j] == target:
#             print(f"{[i,j]}:{nums[i],nums[j]}")

# ------------loop-dict-------------

# nums = [7,2,3,11,15,6]
# target = 9

# def twoSum(nums,target):
#     result = {}
#     for i in range(len(nums)):
#         tumleyen = target - nums[i]
#         if tumleyen in result:
#             return [result[tumleyen],i]
#         result[nums[i]] = i 
    
#     return result

# print(twoSum(nums, target))


# --------------------------------------
# OOP

class Toyota:

    # yapici method , constructor method
    def __init__(self,engine, door, model, color,roof):
        # self.engine --> obje ozelligimiz / en: object attribute
        # engine , door , ... parameter
        self.engine = engine
        self.door = door
        self.model = model
        self.color = color
        self.roof = roof

    # instance method / ornek metot
    def p_info(self):
        return f"engine:{self.engine},door:{self.door},model:{self.model},color:{self.color},roof:{self.roof}"


corolla = Toyota(1.6,4,'corolla 2025', ['black','white'],False)
chr = Toyota(1.6,4,'chr 2025', ['black','white'],True)


# print(corolla.color)
# print(corolla.model)
# print(corolla.engine)

print(corolla.p_info())
print(chr.p_info())