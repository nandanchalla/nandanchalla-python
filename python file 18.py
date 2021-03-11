class amazon (phone):

    __offers="free headset"
    emi   =  "6 months "
    __cashback=5000


    def __init__(self , inch , brand , price):
        super().__init__(inch , brand , price )

    def offers(self):
        print(self.__offers,self.emi,self.__cashback )

    def warranty(self):
        print("6 months warranty")

venkatesh = Amazon(14 , "iphone",54000)
venkatesh.getprice(45000)
venkatesh.buyphone(16, "samsung",14000)
venkatesh.display()
venkatesh.offers()
venkatesh.warranty()
