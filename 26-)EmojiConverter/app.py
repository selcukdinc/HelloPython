emojiConverter = {
    ":)": "🙂",
    ":D": "😃",
    ":(": "😔",
    ">:(": "😫",
    ":')": "🥲",
    ":p": "😛",
    ";p": "😜",
    ":/": "🫤"
}
# Version1 , while loop (student ver.)
while True:
    userInput = input("> ")
    if userInput == "help":
        print("quit - exit the app")
    elif userInput == "quit":
        break
    else:
        for key in emojiConverter:
            searchIndex = userInput.find(key)
            if searchIndex >= 0:
                userInput = userInput.replace(key, emojiConverter.get(key))
        print(userInput)

# Version2 , Teacher version
message = input("> ")
words = message.split(' ')
output = ""
for word in words:
    output += emojiConverter.get(word, word) + " "
print(output)