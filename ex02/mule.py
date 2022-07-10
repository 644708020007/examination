from ex02.house import Horse
from ex02.donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str, age:int, weight:float) -> None:
        super().__init__(name,color,age,weight)

    def run(self):
        return self.run

    def show_info(self):
        return(f'Name{self.name}n\Color{self.color}n\Old{self.age}n\Weight{self.weight}')
        

if __name__ == "__main__":
    print("**********Mumu Info*********")
    m1 = Mule("Mumu","Blue-eye cream",3,200)
    m1.max_height
    m1.show_info()

    print("**********Meme Info*********")
    m2 = Mule("Meme","Palomino",1,120.7)
    m2.sound
    m2.max_height
    m2.show_info()
