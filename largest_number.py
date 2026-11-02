my_list=['1','2','4','6','7','34','22','45']

def largest_number(my_list):
    largest=int(my_list[0])
    for num in my_list:
        num_int = int(num)
        if   num_int > largest:
            largest=num_int
    return largest   
if __name__=="__main__":
     try:
         result=largest_number(my_list)
         print(result)

     except Exception as e:
         print(e)
       