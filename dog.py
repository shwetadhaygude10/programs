class Dog:
     def __init__(self,name,age,bark_sound):
          self.name=name
          self.age=age
          self.bark_sound=bark_sound


     def bark(self):
               print("usually bark")
d1=Dog(name="labra",age=2,bark_sound="usually bark from unknown person")            
print(d1.bark())
print(d1.name)
