# ======================= Task


class Terminal:

    def __init__(self, number, pin) -> None:
        
        if len(str(number)) == 16:
            self.__number = number
        else:
            raise Exception('The length of the Card number must be equal to 16!')
        if len(str(pin)) == 4:
            self.__pin = pin
        else:
            raise Exception('The length of the pin cod must be equal to 4!')

        self.__card = 0
    
    def put(self, pin, som):
        if pin == self.__pin:
            self.__card += som
            return 'Replenishment was successful!'
        else:
            return 'Wrong pin cod!'
        
    def get_money(self, pin, som):
        if pin == self.__pin and som <= self.__card:
            if som%10==0:

                self.__card -= som
                return f'Withdrawed: {som}. Left: {self.__card}.'
            
            else:

                while True:
                    som += 1
                    if som%10==0:
                        break

                self.__card -= som
                return f'Withdrawed: {som}. Left: {self.__card}.'
        else:
            return 'Wrong pin cod or sum out off range your balance'
        
    
kevin = Terminal(9898989898989898, 9898)
print(kevin.put(9898, 5200))
print(kevin.get_money(9898, 401))
print(kevin.get_money(9898, 701))
print(kevin.get_money(9898, 800))
print(kevin.get_money(9898, 900))