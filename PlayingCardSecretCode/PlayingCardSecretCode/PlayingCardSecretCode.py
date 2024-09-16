import math
import code_translator
import bigInt


# translator = code_translator.code_translator()

# for item,i in enumerate(list(range(1000)),start=9007199254740000):
#   message = translator.messageFromIndex(item)
#   # print(item)
#   # print("message: ", message)
#   encoded = translator.encode(message)
#   decoded = translator.decode(encoded)
#   # print("decoded: ", decoded)
#   diffs = ""
#   for i,ltr in enumerate(message):
#     diffs += "_" if ltr == decoded[i] else "X"
#   print(f"[{item}]  diffs: ", diffs)
#   # print("******************")
# # encodeA = translator.encode("B")
# # print(encodeA)
# # decodeA = translator.decode(encodeA)
# # print(decodeA)

# print(9007199254740993)
# print(9007199254740993%100000)
# print(9007199254740993-9007199254740993%100000)

biggy = bigInt.bigInt(987654321)
tiny  = bigInt.bigInt(123456789)
both  = biggy.multiply(tiny)
biggy.reveal()
tiny.reveal()
both.reveal()

# print(int(9007199254740993))
# print(9007199254740993)