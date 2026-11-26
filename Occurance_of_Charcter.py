input_string="apple"
char_count={}
def Occurance_of_Charcter(input_string):
     for char in input_string:
       if char in char_count:
           char_count[char]+=1
       else:
           char_count[char]=1
     return(char_count)

print(Occurance_of_Charcter(input_string))
           
