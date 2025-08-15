# 次のコードが正しく動作するような Square クラスを実装してください
# diagonal は 対角線(の長さ) という意味です。

import math

class Square:
    #コストラクタ
    def __init__(self,side):
        self.side = side
    
    #areaメソッド
    def area(self):
        area_value = self.side * self.side
        if int(area_value) % 1 == 0:
            return f"{area_value}"
        else:
            return f"{area_value:.2f}"
    
    #diagonalメソッド
    def diagonal(self):
        return f"{math.sqrt( self.side **2 + self.side **2 ):.2f}"

square1 = Square(side=1.5)
print(square1.area())  # 2.25
print(square1.diagonal())  # 2.12

square2 = Square(side=15)
print(square2.area())  # 225
print(square2.diagonal())  # 21.21
