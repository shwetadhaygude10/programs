list=[1,2,3,4,5,5,5,6,7,6,]
remove=[]
def RemoveDuplicates(list:int)->int:
    for i in list:
        if i not in remove:
            remove.append(i)
    return remove

print(RemoveDuplicates(list))