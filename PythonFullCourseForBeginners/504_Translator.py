
dict = {
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
}

NumbersToTranslate = input("Give me your numbers: ")
WrittenNumber = ""

for number in NumbersToTranslate:
    WrittenNumber += dict.get(number, "!") + " "

print(WrittenNumber)

#--------------------------

printedMessage = ""
emojies ={
    ":)" : "😊",
    ":(" : "😕",
}
message = input(">")

words = message.split(" ") #uses the space as a separator for multiple words
#print(words)

for word in words:
    printedMessage += emojies.get(word, word) + " "
print(printedMessage)