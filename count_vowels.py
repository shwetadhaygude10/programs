def count_vowels(text:str)->int:
    if not isinstance(text,str):
        raise TypeError("enter only Strings")
    vowels="aeiou"
    count=0
    for char in text.lower():
        if char in vowels:
          count=count+1
    return count
if __name__=="__main__":
    try:
        user_input=input("enter string:=")
        result=count_vowels(user_input)
        print(f"Number of vowels: {result}")

    except TypeError as e:
        print(e)

    except Exception as e:
        print(e)


