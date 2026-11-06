
def reverse_string(input_string):
     if not isinstance(input_string,str): #isisntance is check the input is string or not 
       raise TypeError("enter only string") #if the input is not string it will raise an typrerror

     rev_str=""
     for char in input_string:  #reverse string logic
        rev_str=char+rev_str
     return rev_str
if __name__=="__main__": #main function
     try:
           user_input=input("enter your string to reverse: ")# try and catch errors
           result=reverse_string(user_input)
           print(f"revserse string: {result}")

     except TypeError as e:
          
          print(e)
     except Exception as e:
         print(e)     


