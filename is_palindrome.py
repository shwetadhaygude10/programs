def is_palindrome(text:str)->bool:
     if not isinstance(text,str):
          raise TypeError("enter only stirngs")
     if text.strip()==" ":
          raise ValueError("Input string cannotbe empty")
     else:
          text=text.strip().lower()

     reverse_string=""
     for ch in text:
          reverse_string=ch+reverse_string
     return reverse_string
if __name__=="__main__":
     try:
          user_input=input("enter string: ").strip().lower()
          if is_palindrome(user_input):
               print(f"{user_input} is a palindrome")
               
          else:
                print(f"'{user_input}'  not a palindrome")
               
     except(TypeError,ValueError) as e:
          print("error", e)
          
          
