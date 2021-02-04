# define function to get emojis
def emojis_converter(message):
    # split the message
    words = message.split(" ")

    # define a dictionary of emojis
    emojis = {":)": "😃", ":(": "😒"}

    # define output
    output = ""

    # loop on words to get output
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# get the message
message = input("> ")
print(emojis_converter(message))