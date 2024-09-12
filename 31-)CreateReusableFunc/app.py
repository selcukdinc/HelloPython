def emoji_converter(_message):
    emojis = {
        ":)": "🙂",
        ":D": "😃",
        ":(": "😔",
        ">:(": "😫",
        ":')": "🥲",
        ":p": "😛",
        ";p": "😜",
        ":/": "🫤"
    }
    words = _message.split()
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input("> ")
print(emoji_converter(message))
