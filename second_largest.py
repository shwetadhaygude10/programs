numlist=[10,2,3,1,5,4,272]
def second_largest(numlist:list[int]) -> int :
    if numlist[0]>numlist[1]:
       largest=numlist[0]
       second=numlist[1]
    else:
        largest=numlist[0]
        second-numlist[1]
    for current_number in numlist[2:]:
        if current_number > largest:
            second = largest       
            largest = current_number
        elif  current_number is largest and current_number > second:
            second=current_number
    return(second)

print(second_largest(numlist))
