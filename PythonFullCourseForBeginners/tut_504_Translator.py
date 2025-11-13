
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

numbers_to_translate = input("Give me your numbers: ")
written_number = ""

for number in numbers_to_translate:
    written_number += dict.get(number, "!") + " "

print(written_number)

#--------------------------

printed_message = ""
emojies ={
    ":)" : "😊",
    ":(" : "😕",
}
message = input(">")

words = message.split(" ") #uses the space as a separator for multiple words
#print(words)

for word in words:
    printed_message += emojies.get(word, word) + " "
print(printed_message)