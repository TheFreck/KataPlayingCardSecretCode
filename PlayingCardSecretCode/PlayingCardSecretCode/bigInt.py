class bigInt(object):
    def __init__(self,digits):
        if type(digits) == bigInt:
            self.stringified = digits.stringified
        else:
            self.stringified = str(digits)
        print(self.stringified)
        self.length = len(self.stringified)
        self.halfLen = int(self.length/2)
        self.tail = str(int(self.stringified[self.halfLen:])).rjust(self.length,"0")
        self.head = str(int(self.stringified[:self.halfLen])).ljust(self.length,"0")
        
    def reveal(self):
        print(f'{{\n  stringified: {self.stringified},\n  length: {self.length},\n         head: {self.head},\n         tail: {self.tail}')

    def multiply(self,number):
        if type(number) != bigInt:
            print("num*head: ", number * self.head)
            print("num*tail: ", number * self.tail)
            outcome = bigInt(number * self.head + number * self.tail)
        else:
            hh = int(self.head)*int(number.head)
            ht = int(self.head)*int(number.tail)
            th = int(self.tail)*int(number.head)
            tt = int(self.tail)*int(number.tail)
            hhLen = len(str(hh))
            htLen = len(str(ht))
            thLen = len(str(th))
            ttLen = len(str(tt))
            theMax = max(hhLen,htLen,thLen,ttLen)
            hhJust = str(hh).rjust(theMax,"0")
            htJust = str(ht).rjust(theMax,"0")
            thJust = str(th).rjust(theMax,"0")
            ttJust = str(tt).rjust(theMax,"0")
            
            outcome = ""
            carry = "0"
            for digit in range(theMax):
                a = int(hhJust[-1-digit])
                b = int(htJust[-1-digit])
                c = int(thJust[-1-digit])
                d = int(ttJust[-1-digit])
                num = a + b + c + d + int(carry)
                print(num)
                dgt = int(num % 10)
                print("dgt: ", dgt)
                carry = str(num - dgt)[0] if num-dgt > 1 else "0"
                print("cry: ", carry)
                outcome = str(dgt) + outcome
        print("outcome: ", outcome)
        return bigInt(outcome)