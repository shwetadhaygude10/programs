
def reverse_string(input_string):
     if not isinstance(input_string,str):
       raise TypeError("enter only string")

     rev_str=""
     for char in input_string:
        rev_str=char+rev_str
     return rev_str
if __name__=="__main__":
     try:
           user_input=input("enter your string to reverse: ")
           result=reverse_string(user_input)
           print(f"revserse string: {result}")

     except TypeError as e:
          
          print(e)
     except Exception as e:
         print(e)     


