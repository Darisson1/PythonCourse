
def convert_text_to_emojie(message):
    converted_message = ""
    splitted_text = message.split(" ")
    for words in splitted_text:
        converted_message += emojies.get(words, words) + " "
    return converted_message

emojies ={
    ":)" : "😊",
    ":(" : "😕",
}



message = input(">")

print(convert_text_to_emojie(message))
