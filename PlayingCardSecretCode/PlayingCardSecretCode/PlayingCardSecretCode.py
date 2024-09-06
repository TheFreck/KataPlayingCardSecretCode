from math import factorial


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


# cards = ["AC","2C","3C","4C","5C","6C","7C","8C","9C","TC","JC","QC","KC",
#         "AD","2D","3D","4D","5D","6D","7D","8D","9D","TD","JD","QD","KD",
#         "AH","2H","3H","4H","5H","6H","7H","8H","9H","TH","JH","QH","KH",
#         "AS","2S","3S","4S","5S","6S","7S","8S","9S","TS","JS","QS","KS"]

cards = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14',
         '15','16','17','18','19','20','21','22','23','24','25','26','27','28',
         '29','30','31','32','33','34','35','36','37','38','39','40','41','42',
         '43','44','45','46','47','48','49','50','51','52']

# cards = ["a","b","c","d"]

# cards = ["0","1","2","3","4","5","6","7","8","9"]

def encode(message):
    val = getMsgValue(message)
    perm = permFromIndex(val,len(cards))
    symbols = convertToSymbols(perm,cards)
    return symbols

def getMsgValue(message):
    messageList = []
    messageValue = 0
    for i,letter in enumerate(message):
        messageList.append(letterValues[letter])
        messageValue += letterValues[letter]*27**(len(message)-(i+1))
    return messageValue

def permFromIndex(index,symbolCount):
    order = []
    enumerated = list(enumerate(range(symbolCount),start=1))
    # print("index: ", index)
    for item in reversed(enumerated):
        fact = factorial(item[0])
        position = index % fact
        block = int(index%fact)
        if item[0] == 2:
            block = index % 2
        if item[0] == 1:
            block = (index+1)%2
        order.append(block)
    # print("order: ,", order)
    return order

def convertToSymbols(order,symbols):
    theSymbols = symbols[:]
    output = []
    
    for item in enumerate(order):
        output.append(theSymbols.pop(item[1]) if item[1] < len(theSymbols) else theSymbols.pop())
    return output

def decode(code):
    return "decoded"

print("*******")
# print(0,permFromIndex(0,52))
# print(1,permFromIndex(1,52))
# print(2,permFromIndex(2,52))
# print(3,permFromIndex(3,52))
# print(4,permFromIndex(4,52))
# print(5,permFromIndex(5,52))
# print(6,permFromIndex(6,52))
# print(7,permFromIndex(7,52))
# print(8,permFromIndex(8,52))
# print(9,permFromIndex(9,52))
# print(10,permFromIndex(10,52))
# print(11,permFromIndex(11,52))
# print(12,permFromIndex(12,52))
# print(13,permFromIndex(13,52))
# print(14,permFromIndex(14,52))
# print(15,permFromIndex(15,52))
# print(16,permFromIndex(16,52))
# print(17,permFromIndex(17,52))
# print(18,permFromIndex(18,52))
# print(19,permFromIndex(19,52))
# print(20,permFromIndex(20,52))
# print(21,permFromIndex(21,52))
# print(22,permFromIndex(22,52))
# print(23,permFromIndex(23,52))
# print(24,permFromIndex(24,52))
# print(25,permFromIndex(25,52))
# print(26,permFromIndex(26,52))
# print(27,permFromIndex(27,52))
# print(28,permFromIndex(28,52))
# print(29,permFromIndex(29,52))
# print(30,permFromIndex(30,52))
# print(31,permFromIndex(31,52))
# print(32,permFromIndex(32,52))
# print(33,permFromIndex(33,52))
# print(34,permFromIndex(34,52))
# print(35,permFromIndex(35,52))
# print(36,permFromIndex(36,52))
# print(37,permFromIndex(37,52))
# print(38,permFromIndex(38,52))
# print(39,permFromIndex(39,52))
# print(40,permFromIndex(40,52))

for permutation in range(200):
    print(str(permutation) if permutation > 9 else "0" + str(permutation),str(permFromIndex(permutation,52)))

# print("*******")
# print(" ")
# print(encode(" "))
# print("*******")
# print("A")
# print(encode("A"))
# print("*******")
# print("B")
# print(encode("B"))
# print("*******")
# print("C")
# print(encode("C"))
# print("*******")
# print("D")
# print(encode("D"))
# print("*******")
# print("E")
# print(encode("E"))
# print("*******")
# print("F")
# print(encode("F"))
# print("*******")
# print("G")
# print(encode("G"))
# print("*******")
# print("X")
# print(encode("X"))
# print("*******")
# print("Y")
# print(encode("Y"))
# print("*******")
# print("Z")
# print(encode("Z"))
# print("*******")
# print("A ")
# print(encode("A "))
# print("*******")
# print("AA")
# print(encode("AA"))
# print("*******")
# print("AB")
# print(encode("AB"))
# print("*******")
# print("AC")
# print(encode("AC"))
# print("*******")
# print("AY")
# print(encode("AY"))
# print("*******")
# print("AZ")
# print(encode("AZ"))
# print("*******")
# print("AA ")
# print(encode("AA "))
# print("*******")
# print("AAA")
# print(encode("AAA"))
# print("*******")
# print("AAB")
# print(encode("AAB"))
# print("*******")
# print("AAC")
# print(encode("AAC"))

# print("ATTACK TONIGHT ON CODEWARS")
# result = encode("ATTACK TONIGHT ON CODEWARS")
# print(result)

# answerCards = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","24","22","46","48","25","44","36","20","49","51","28","50","32","42","45","23","47","41","34","33","43","30","29","31","40","39","38","35","36","52","37","21","27"]
# errors = []

# for card in enumerate(answerCards):
#     print(f'[{card[0]}] {card[1]}: {result[card[0]]} {True if card[1] == result[card[0]] else False}')

