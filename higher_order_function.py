def calculator(nums,func):
    return func(nums)

def square(number):
    return number*number

def cube(num):
    return num*num*num


result=calculator(5,square)
res=calculator(3,cube)
print(result)
print(res)