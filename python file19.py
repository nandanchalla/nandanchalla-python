class  phone:

    def __init__ (self,inch,brand,price):
        self.__specifi = []
        self.__specifi.append(inch)
        self.__specifi.append(brand)
        self.__specifi.append(price)

    def getprice(self,price):

        for i in self.specifi:

            if i == price :
                print ("found a phone")
            else:
                continue


    def buyphone (self,*args ):
        for i in args :
         self.__specifi.append(i)

    def display(self):
        print(self.__specifi)

    def warranty(self):
        print("1 year warranty")

    def __del__(self):
        print("phone destructor")


venkatesh = phone(14 , "iphone",54000)
venkatesh.getprice(45000)
venkatesh.buyphone(16 , "samsung" , 14000)
venkatesh.display()
