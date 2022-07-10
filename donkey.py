class Donkey:

    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print ('Donkey makes eeyore sound')

    def show_info(self):
        return f'{self.age}-year-old\n{self.weight} kg'