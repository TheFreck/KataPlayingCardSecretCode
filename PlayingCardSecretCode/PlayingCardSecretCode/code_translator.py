import math
from pickletools import stringnl

class code_translator(object):
    letters = [
        " ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    letterValues = {
            " ": 0,
            "A": 1,
            "B": 2,
            "C": 3,
            "D": 4,
            "E": 5,
            "F": 6,
            "G": 7,
            "H": 8,
            "I": 9,
            "J": 10,
            "K": 11,
            "L": 12,
            "M": 13,
            "N": 14,
            "O": 15,
            "P": 16,
            "Q": 17,
            "R": 18,
            "S": 19,
            "T": 20,
            "U": 21,
            "V": 22,
            "W": 23,
            "X": 24,
            "Y": 25,
            "Z": 26
            }

    cards = ["AC","2C","3C","4C","5C","6C","7C","8C","9C","TC","JC","QC","KC",
            "AD","2D","3D","4D","5D","6D","7D","8D","9D","TD","JD","QD","KD",
            "AH","2H","3H","4H","5H","6H","7H","8H","9H","TH","JH","QH","KH",
            "AS","2S","3S","4S","5S","6S","7S","8S","9S","TS","JS","QS","KS"]

    cardValues = {"AC":1,"2C":2,"3C":3,"4C":4,"5C":5,"6C":6,"7C":7,"8C":8,"9C":9,"TC":10,"JC":11,"QC":12,"KC":13,
            "AD":14,"2D":15,"3D":16,"4D":17,"5D":18,"6D":19,"7D":20,"8D":21,"9D":22,"TD":23,"JD":24,"QD":25,"KD":26,
            "AH":27,"2H":28,"3H":29,"4H":30,"5H":31,"6H":32,"7H":33,"8H":34,"9H":35,"TH":36,"JH":37,"QH":38,"KH":39,
            "AS":40,"2S":41,"3S":42,"4S":43,"5S":44,"6S":45,"7S":46,"8S":47,"9S":48,"TS":49,"JS":50,"QS":51,"KS":52}
    
    def __init__(self):
        self
        
    def encode(self,message):
        index = self.indexFromMessage(message)
        order = self.orderFromIndex(index,len(self.cards))
        symbols = self.symbolsFromOrder(order,self.cards)
        return symbols

    def decode(self,symbols):
        order = self.orderFromSymbols(symbols)
        index = self.indexFromOrder(order)
        message = self.messageFromIndex(index)
        return message

    # *********************************************************************
    # encode helpers
    # *********************************************************************
    def indexFromMessage(self,message):
        messageList = []
        messageValue = 0
        for i,letter in enumerate(message):
            messageList.append(self.letterValues[letter])
            messageValue += self.letterValues[letter]*27**(len(message)-(i+1))
        return messageValue

    def orderFromIndex(self,index,symbolCount):
        order = []
        orderCards = []
        enumerated = list(enumerate(range(symbolCount),start=1))
        for i,place in reversed(enumerated):
            fact = math.factorial(place)
            gSize = fact/i
            a = int(index/fact) % i
            order.append(a)
        return order

    def symbolsFromOrder(self,order,symbols):
        theSymbols = symbols[:]
        output = []
    
        for i,item in enumerate(order):
            c = self.cards[item]
            output.append(theSymbols.pop(item))
        return output
    

    # *********************************************************************
    # decode helpers
    # *********************************************************************
    def orderFromSymbols(self,cardsIn):
        theCards = self.cards[:]
        order = []
        for card in cardsIn:
            order.append(theCards.index(card))
            theCards.remove(card)
        return order

    def indexFromOrder(self,order):
        index = 0
        for p,val in enumerate(order):
            place = len(order)-p
            addToIndex = val*math.factorial(place-1)
            index += addToIndex
        return index

    def messageFromIndex(self,index):
        message = ""
        val = index
        remainder = 0
        message = self.letters[val%27] + message
        val = int(val/27)
        while (val > 0):
            message = self.letters[val%27] + message
            val = int(val/27)
        return message
