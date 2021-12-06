#Program to find area and volume using oops concept
class Area:
    # def __init__(self):
    #     self.area = 10
    def calA(self):
        # print(self.area)
        length = int(input("Enter length "))
        bredth= int(input("Enter Bredth "))
        area = length*bredth
        return area

class Vol(Area):
    def __init__(self):
        pass
    def calV(self):
        height= int(input("Enter Height "))
        volume=self.calA()*height
        return volume
class Print(Vol):
    def viwe(self):
        print("Area of rectangle is : ",self.calA())
        print("Volume of the cube is : ",self.calV())
obj = Area()
obj.calA()

