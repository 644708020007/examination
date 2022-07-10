class Horse:
    max_height = 200

    def __init__(self,name:str,color:str) -> None:
        self.name = name
        self.color = color
        

    def run(self):
        return f'{self.name} is running'

    def show_name(self):
        return f'Name:{self.name}'

    def show_info(self):
        return f'Name: {self.name}\nColor: {self.color}\nMax Height:{Horse.max_height}'



    