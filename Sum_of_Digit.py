
def Sum_of_digit(num:int)->int:
    if not isinstance(num,int):
        raise TypeError(" number must be integer")
    if num <0:
        raise ValueError("number must be non negative")
    total=0
    while num > 0:
        total=total+num %10  #this logic will take an  reminder of 123 is 3

        num=num//10        # num//10=12
    return total

if __name__=="__main__":
    try:
        num=int(input("enter your number: "))
        result=Sum_of_digit(num)
        print(f"{result} this is sum of digit")
    except (TypeError,ValueError) as e:
        print(e)
    

        