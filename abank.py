from bank import Bank

class Abank(Bank):
    def __init__(self,interest:float,pay:float) -> None:
        self.__loanamount = 0
        self.__loanyear = 0
        self.__loanrate = 0
        self.interest = interest
        self.mounthlypay = pay

    @property
    def loanamount(self):
        return self.__loanamount
    
    @property
    def loanyear(self):
        return self.__loanyear
    
    @property
    def loanrate(self):
        return self.__loanrate

    @loanamount.setter
    def loanamount(self,value):
        self.__loanamount = value
    
    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    @loanyear.setter
    def loanyear(self,value):
        self.__loanyear = value

    def flat_rete(self):
        super().flat_rate()
        self.interest = self.loanamount * (self.loanrate / 100) * self.loanyear
        self.mounthlypay = (self.loanamount + self.interest) / (self.loanyear * 12)
   
    def display_interest(self):
        print(f"*******{self.bankname}*********")
        print(f"Loan:{self.loanamount:.2f} bath")
        print(f"Rate: {self.loanrate:.2f} %")
        print(f'year{self.loanyear}')

        print("--Interest--")
        print(f"Interset:{self.interest:.2f} bath")
        print(f"Monthly Repayment:{self.mounthlypay:.2f} bath")
        




        


