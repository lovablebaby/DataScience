
# coding: utf-8

# In[ ]:

# -*- coding: cp949 -*-


class Fridge:
    
    def __init__(self):
        self.isOpened = False
        self.foods = []
        
    def open(self):
        self.isOpened = True
        print("냉장고 문을 열었습니다")
        
    def putItem(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print("냉장고 속에 음식을 넣었습니다")
        else:
            print("냉장고 문이 닫혀있어서 불가능합니다")
            
    def close(self):
        self.isOpened = False
        print("냉장고 문을 닫았습니다")
        
class Food:
    pass

