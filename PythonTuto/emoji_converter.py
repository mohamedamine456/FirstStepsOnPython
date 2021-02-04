# get the message
message = input("> ")

# split the message
words = message.split(" ")

# define a dictionary of emojis
emojis = {":)": "😃", ":(": "😒"}

# define output
output = ""

# loop on words to get output
for word in words:
    output += emojis.get(word, word) + " "

print(output)